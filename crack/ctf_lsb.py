from PIL import Image

def text_to_binary(text):
    """将文本转换为二进制字符串"""
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def encode_message(image_path, message):
    """将消息编码到图像中"""
    image = Image.open(image_path)
    binary_message = text_to_binary(message)
    message_length = len(binary_message)

    # 检查消息是否可以嵌入到图像中
    if message_length * 3 > image.width * image.height:
        print("Error: Message is too large to be encoded in the image.")
        return None

    data_index = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                if data_index < message_length:
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            image.putpixel((x, y), tuple(pixel))

            if data_index >= message_length:
                break
        if data_index >= message_length:
            break

    image.save("encoded_image.png")
    print("Message encoded successfully.")

def decode_message(image_path):
    """从图像中解码消息"""
    image = Image.open(image_path)
    binary_message = ""

    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            for color in pixel:
                binary_message += str(color & 1)

    # 从二进制消息中提取原始文本
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    return message

# 测试隐写术的编码和解码
message = "Hello, this is a hidden message!"
encode_message("/home/liuty/Pictures/2024-02-16_10-34.png", message)
decoded_message = decode_message("/home/liuty/Pictures/encoded_image.png")
print("Decoded message:", decoded_message)