import base64
import io
import os
import pathlib
import onnxruntime
import pkg_resources
import torch
import torchvision
from PIL import Image, UnidentifiedImageError


class QiAlgo_OCR:
    def __init__(self):
        self.device = None
        self.ort_session = None
        self.charset = None
        self.image = None

        self.init_device()
        self.init_charset()

    class TypeError(Exception):
        pass

    def init_device(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def init_charset(self):
        self.charset = [' ', '5', 'N', 'R', 'J', 'n', 'E', 'v', 'Q',
                        'g', '7', '9', 'X', '2', 'Y', 'D', 't', 'x',
                        'r', '1', 'o', 'C', 'k', 'e', 'p', 'G', 'i',
                        'S', 'l', 'P', 'I', '3', 'L', 'c', 'z', 'f',
                        's', 'V', 'H', 'T', 'd', 'm', '0', 'y', '4',
                        '6', 'w', 'b', 'q', 'W', 'O', 'a', 'F', 'B',
                        'A', 'h', 'U', 'Z', 'K', 'M', 'j', '8', 'u']

    def init_onnx_module(self):
        if torch.cuda.is_available():
            providers = [
                ('CUDAExecutionProvider', {
                    'arena_extend_strategy': 'kNextPowerOfTwo',
                    'gpu_mem_limit': 2 * 1024 * 1024 * 1024,  # 2 * 1 GB
                    'cudnn_conv_algo_search': 'EXHAUSTIVE',
                    'do_copy_in_default_stream': True,
                }),
            ]
        else:
            providers = [
                'CPUExecutionProvider',
            ]

        self.ort_session = onnxruntime.InferenceSession(
            pkg_resources.resource_filename('QiAlgo_OCR', 'model/model.onnx'),
            providers=providers
        )

    def load_image(self, image):
        """
        加载图片
        :param image: 字节序列、Base64、路径、PIL（Pillow）库中的Image图像对象、PurePath路径
        :return:
        """
        # 检查图片类型
        if not isinstance(image, (bytes, str, pathlib.PurePath, Image.Image)):
            raise TypeError("The 'image' variable must be of type bytes, base64, pathlib.PurePath, or Image.Image.")

        # 初始化变量
        base_height = 64
        color_channel = 'L'

        # 加载图片
        if isinstance(image, bytes):
            image = Image.open(io.BytesIO(image))
        if isinstance(image, str):
            try:
                image = Image.open(io.BytesIO(base64.b64decode(image)))
            except (base64.binascii.Error, UnidentifiedImageError):
                if os.path.exists(image):
                    image = Image.open(image)
                else:
                    raise TypeError(
                        "The 'image' variable must be of type bytes, base64, pathlib.PurePath, or Image.Image."
                    )
        if isinstance(image, pathlib.PurePath):
            image = Image.open(image)
        if isinstance(image, Image.Image):
            image = image.copy()

        # 改变图片大小
        image_width, image_height = image.size
        base_width = int(image_width * (base_height / image_height))
        image = image.resize((base_width, base_height)).convert(color_channel)

        transform_list = [
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean=[0.456], std=[0.224])
        ]
        transform = torchvision.transforms.Compose(transform_list)

        image_transform = transform(image)

        self.image = image_transform.unsqueeze(0).to(self.device)

    def onnx_predictor(self):
        """
        使用onnx模型的预测函数
        :return: 代表是否成功的布尔值, 预测的字符串
        """
        # 加载模型
        self.init_onnx_module()

        # 构建模型输入
        onnx_module_input = {self.ort_session.get_inputs()[0].name: self.image.cpu().numpy()}
        # 获取模型预测标签索引
        onnx_predicted_labels = self.ort_session.run(
            None, onnx_module_input
        )[0][0]

        # 存放预测的字符串
        onnx_predicted_str = []
        last_label_int = 0
        for label_int in onnx_predicted_labels:
            if label_int == last_label_int:
                continue
            else:
                last_label_int = label_int
            if label_int != 0:
                onnx_predicted_str.append(self.charset[label_int])

        if onnx_predicted_str:
            return True, ''.join(onnx_predicted_str)
        else:
            return False, None
