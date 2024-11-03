print("hello world")
from PIL import Image

def compress_image(input_path, output_path, quality=85, resize_factor=0.5):
    # 開啟圖片
    with Image.open(input_path) as img:
        # 調整圖片大小（例如縮小至原始大小的50%）
        new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
        img = img.resize(new_size)
        

        
        # 儲存圖片並調整品質
        img.save(output_path, "JPEG", quality=quality)

# 使用範例
compress_image("p1.png.JPG", "output.jpg", quality=80, resize_factor=0.5)




