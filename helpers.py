import os
from jogoteca import app


def get_image(id):
    for image_name in os.listdir(app.config['UPLOADS_PATH']):
        if f'capa-{id}' in image_name:
            return image_name

    return 'capa_padrao.jpg'

def remove_image(id):
    image = get_image(id)

    if image != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOADS_PATH'], image))