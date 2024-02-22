import numpy as np
import gradio as gr
import os
import pdb # #pdb.set_trace()
import backend_test


def upload_files(file1, file2):
    file1_path = [file.name for file in file1]
    file2_path = [file.name for file in file2]
    #file_paths = [file1.name, file2.name]
    #print(file_paths)
    output = backend_test.start(file1_path, file2_path, os.path.dirname(file2.name))
    return output

with gr.Blocks() as demo:
    gr.Markdown("텍스트 분석") # 제목표시

    # with gr.Tab("시작"):
    with gr.Row():
        #gr.Markdown("법무팀의 워드파일을 을 왼쪽에 사용자의 워드파일을 오른쪽에 넣어주세요")

        text_input1 = gr.File(label="법무팀 워드파일 입력",file_count="single", file_types=['.docx'])
        text_input2 = gr.File(label="비교할 워드파일 입력",file_count="single", file_types=['.docx'])
                #keyfile_name = gr.Interface(tab2_inputs, inputs="file", outputs=None)
                #tab2_inputs = [keyfile_name, tab2_inputs]

    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            gr.Markdown(label="워드파일의 결과를 다운받아주세요")
            text_output = [gr.File(label="비교 결과 파일",
                    file_count="single",
                    file_types=[".docx"])]

    compare_submit_button = gr.Button("비교 시작")
    compare_submit_button.click(upload_files, inputs=[text_input1,text_input2], outputs=text_output)
    #compare_submit_button.click(upload_files, inputs=[text_input1,text_input2], outputs=text_output)


# demo.launch(server_name="0.0.0.0")
# demo.launch( server_name="0.0.0.0",server_port=8000)
demo.launch(share=True)
