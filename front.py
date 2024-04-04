import numpy as np
import gradio as gr
import pdb
import backend
import os

def upload_files(file1, file2):
    file1_path = file1.name
    file2_path = file2.name
    output = backend.start(file1_path, file2_path, os.path.dirname(file2_path)) 
    return output

with gr.Blocks() as demo:
    gr.Markdown("텍스트 분석")

    with gr.Row():
        text_input1 = gr.File(label="법무팀 워드파일 입력",file_count="single", file_types=['.docx'])
        pdb.set_trace()
        text_input2 = gr.File(label="비교할 워드파일 입력",file_count="single", file_types=['.docx'])

    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            gr.Markdown(label="워드파일의 결과를 다운받아주세요")
            text_output = [gr.File(label="비교 결과 파일",
                    file_count="single",
                    file_types=[".docx"])]

    compare_submit_button = gr.Button("비교 시작")
    pdb.set_trace()
    compare_submit_button.click(upload_files, inputs=[text_input1,text_input2], outputs=text_output)

demo.launch(share=True)



