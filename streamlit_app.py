'''Test EasyNMT opus-mt

'''

import streamlit as st
# from easynmt import EasyNMT
# model = EasyNMT('opus-mt')


# ---------- streamlit ----------
# When a user interacts with widgets in the app:
# Streamlit will rerun the code from top to bottom
# ---------- streamlit ----------
st.set_page_config(
    page_title='EasyNMT Testing',
    page_icon='📝',
    layout='wide',
)

st.markdown('Moved to: [https://huggingface.co/spaces/dpc/nmt](https://huggingface.co/spaces/dpc/nmt)')
# with st.container():
#     st.markdown('## 📑 Machine Translation')
#     st.write('Using EasyNMT and opus-mt model.')

# lang_list = model.get_languages()

# b_size = st.slider('Translation quality (Beam size)', 1, 10, 5)

# text = ''
# submit = ''
# target_langs = ''

# with st.form(key='nmt'):
#     text = st.text_area(
#         label='Enter text',
#         placeholder='Enter a sentence. Pāḷi translation is not available now.',
#         help='Auto detect input language 170+.')
#     target_langs = st.multiselect(
#         'Translate to (can select more than one language)',
#         lang_list,
#         ['en', 'vi'])
#     submit = st.form_submit_button(label='Translate')

# if submit and text:
#     detected_lang = model.language_detection(text)

#     st.write('Dectected input language: ' + detected_lang)

#     if not target_langs:
#         st.error('Please choose at least 1 target language.')
#         st.stop()

#     for lang in target_langs:
#         try:
#             res = model.translate(text, target_lang=lang, beam_size=b_size)
#             if res:
#                 st.success(lang + ' => ' + res)

#         except Exception as e:
#             st.write(e)
