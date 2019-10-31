from fastai.vision import open_image, load_learner

# Configs
MODEL_EXPORT = 'export.pkl'
SAMPLE_IMG = 'test_images/1.jpg'

# load pretrained model
learner = load_learner(path='.', file=MODEL_EXPORT)

# load image to be predicted
img = open_image(SAMPLE_IMG)

# image prediction
pred = learner.predict(img)

print(f'data classes: {learner.data.classes}')
print(f'prediction for {SAMPLE_IMG}: {pred}')