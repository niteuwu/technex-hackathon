import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd

st.set_page_config(page_title = 'Showcase', page_icon = ':star:', layout = 'wide')

back_to_top = st.markdown('''
    <div class="container-top" style="--offset: 100px; --fade: 120px; mask: linear-gradient(#0000 calc(100vh + var(--offset)), #000 calc(100vh + var(--offset) + var(--fade)));">
        <a href="#" class="top"></a>
    </div>
''', unsafe_allow_html = True)
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_code = load_lottie('https://assets6.lottiefiles.com/packages/lf20_tfb3estd.json')
img_1_input = Image.open('images/__results___8_1.png')
img_1_output = [
    Image.open('images/__results___8_1.png'),
    Image.open('images/__results___8_4.png'),
    Image.open('images/__results___8_5.png'),
    Image.open('images/__results___8_6.png'),
    Image.open('images/__results___8_7.png'),
]
img_2_input = Image.open('images/__results___9_1.png')
img_2_output = [
    Image.open('images/__results___9_3.png'),
    Image.open('images/__results___9_4.png'),
    Image.open('images/__results___9_5.png'),
    Image.open('images/__results___9_6.png'),
    Image.open('images/__results___9_7.png'),
]
img_3_input = Image.open('images/__results___10_1.png')
img_3_output = [
    Image.open('images/__results___10_3.png'),
    Image.open('images/__results___10_4.png'),
    Image.open('images/__results___10_5.png'),
    Image.open('images/__results___10_6.png'),
    Image.open('images/__results___10_7.png'),
]

with st.container():
    st.subheader('Hi, I am Tanish :wave:')
    st.title('Welcome to my hackathon showcase')
    st.write('[Check out my notebook and try it out yourself >](https://www.kaggle.com/code/eveneverlands/hack-q3/edit/run/122673475)')
    st.write('[Report >](google.com)')

with st.container():
    st.write('---')
    left, right = st.columns(2)
    with left:
        st.header('Index')
        st.write('##')
        st.write('''
            1. Showcase of Example
            2. Review
            3. Dataset
            4. Model Skeleton
            5. Cosine Similarity
            6. Exploratory Data Analysis (EDA)
        ''')
    with right:
        st_lottie(lottie_code, height = 400, key = 'brainstorming')

with st.container():
    st.write('---')
    st.header('Recommendation System Model')
    st.write('##')
    left, right = st.columns((1, 2))
    with left:
        st.image(img_1_input)
    with right:
        for i in img_1_output:
            st.image(i)

with st.container():
    st.write('---')
    left, right = st.columns((1, 2))
    with left:
        st.image(img_2_input)
    with right:
        for i in img_2_output:
            st.image(i)
            
with st.container():
    st.write('---')
    left, right = st.columns((1, 2))
    with left:
        st.image(img_3_input)
    with right:
        for i in img_3_output:
            st.image(i)
            
#------ REVIEW

with st.container():
    st.write('---')
    st.header('Review')
    st.write('##')
    st.write('''
        I'll be talking about my experience here.
    ''')

with st.container():
    st.write('---')
    st.header('Dataset')
    st.write('##')
    df = pd.read_csv('images.csv')
    st.dataframe(df)
    st.write('[Link to Dataset](https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full)')
    
with st.container():
    st.write('---')
    st.header('Model Skeleton')
    st.write('##')
    st.text('''
        Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_1 (InputLayer)        [(None, 224, 224, 3)]     0         
                                                                 
 block1_conv1 (Conv2D)       (None, 224, 224, 64)      1792      
                                                                 
 block1_conv2 (Conv2D)       (None, 224, 224, 64)      36928     
                                                                 
 block1_pool (MaxPooling2D)  (None, 112, 112, 64)      0         
                                                                 
 block2_conv1 (Conv2D)       (None, 112, 112, 128)     73856     
                                                                 
 block2_conv2 (Conv2D)       (None, 112, 112, 128)     147584    
                                                                 
 block2_pool (MaxPooling2D)  (None, 56, 56, 128)       0         
                                                                 
 block3_conv1 (Conv2D)       (None, 56, 56, 256)       295168    
                                                                 
 block3_conv2 (Conv2D)       (None, 56, 56, 256)       590080    
                                                                 
 block3_conv3 (Conv2D)       (None, 56, 56, 256)       590080    
                                                                 
 block3_pool (MaxPooling2D)  (None, 28, 28, 256)       0         
                                                                 
 block4_conv1 (Conv2D)       (None, 28, 28, 512)       1180160   
                                                                 
 block4_conv2 (Conv2D)       (None, 28, 28, 512)       2359808   
                                                                 
 block4_conv3 (Conv2D)       (None, 28, 28, 512)       2359808   
                                                                 
 block4_pool (MaxPooling2D)  (None, 14, 14, 512)       0         
                                                                 
 block5_conv1 (Conv2D)       (None, 14, 14, 512)       2359808   
                                                                 
 block5_conv2 (Conv2D)       (None, 14, 14, 512)       2359808   
                                                                 
 block5_conv3 (Conv2D)       (None, 14, 14, 512)       2359808   
                                                                 
 block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         
                                                                 
 flatten (Flatten)           (None, 25088)             0         
                                                                 
 fc1 (Dense)                 (None, 4096)              102764544 
                                                                 
 fc2 (Dense)                 (None, 4096)              16781312  
                                                                 
=================================================================
Total params: 134,260,544
Trainable params: 134,260,544
Non-trainable params: 0
_________________________________________________________________
    ''')

with st.container():
    st.write('---')
    st.header('Consine Similarity')
    st.write('##')
    st.image(Image.open('images/proxy-image.png'))
    
with st.container():
    st.write('---')
    st.header('EDA')
    st.write('##')
    st.write('[Check out this page](file:///home/tanish/Desktop/jupyter/pages/EDA.html)')