import pygame
import copy
import os

from utils import code_generator

pygame.init()

dir_path = os.path.dirname(os.path.realpath(__file__))
img_path = dir_path + '\\..\\..\\..\\res\\imgs\\'


class ImageRenderer:
    def __init__(self):
        self.requests = []
        self.images = {}
        self.load_images()
        self.define_rects()

    def load_images(self):
        image_files = os.listdir(path=img_path)
        for file in image_files:
            file_name = file.split('.')[0]
            file_extension = file.split('.')[1]

            self.images[file_name] = {
                "image": pygame.image.load(img_path + file).convert(),
                "ext": file_extension
            }

    def define_rects(self):
        self.image_keys = self.images.keys()
        for key in self.image_keys:
            self.images[key]["img_rect"] = self.images[key]["image"].get_rect()
    
    def get_image(self, image:str, center:tuple, size:tuple = None):
        img_to_return = copy.copy(self.images[image])

        if size:

            img_to_return["image"] = pygame.transform.scale(img_to_return["image"], size)
            img_to_return["img_rect"] = img_to_return["image"].get_rect()
            img_to_return["img_rect"].center = center

            return img_to_return

        else:
        
            img_to_return["img_rect"].center = center
            return img_to_return

    def render_image(self, image:str, center:tuple, size:type = None):
        img = self.get_image(image, center=center, size=size)
        
        while True:
            id = code_generator(6)
            unique = True
            for request in self.requests:
                if request[0] == id:
                    unique = False
            
            if unique:
                break
        
        self.requests.append((id, img,))

        return id

    def get_render_requests(self):
        display = []
        for i in range(len(self.requests)):
            img = self.requests[i][1]
            display.append({
                "surface": img["image"],
                "object": img["img_rect"]
            })
        return display

    def remove_image(self, id):
        req_to_remove = None
        for request in self.requests:
            if request[0] == id:
                req_to_remove = request
        
        if req_to_remove:
            self.requests.remove(req_to_remove)
            print(f'{id} removed')
        else:
            print('no image with this id')


"""-------------------------------------------TEST------------------------------------------------"""
# screen = pygame.display.set_mode((500, 500))
# image_renderer = ImageRenderer()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

#     image_renderer.render_image(screen, "fish", (250, 250,), (128, 128,))
#     pygame.display.update()
