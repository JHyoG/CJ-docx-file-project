import gradio as gr
import os
import pdb # #pdb.set_trace()
import backend_test

# 파일 1개씩 넣었다고 가정하고 코드 작성!

def upload_file(file1): # file1 -> 파일객체 , file1.name -> 파일 이름 추출
    file_paths = file1.name 
    return file_paths # -> 수정 필요한 부분

def upload_file_a(file1,file2): 
    file_paths_1 = [file.name for file in file1] 
    file_paths_2 = [file.name for file in file1] 
    return file_paths_1 # -> 수정 필요한 부분


with gr.Blocks() as demo:
    with gr.Group():
        with gr.Row():
            file1_output = gr.File() # -> 파일 출력 객체 생성(업로드된 파일의 내용)
            file2_output = gr.File()
            # pdb.set_trace()
    with gr.Group():
        with gr.Row():
            orgin_upload_button = gr.UploadButton("원본파일을 넣어주세요",file_types=[".docx"],  file_count="single")
            orgin_upload_button.upload(upload_file, orgin_upload_button, file1_output)
            # pdb.set_trace()
            compare_upload_button = gr.UploadButton("비교파일을 넣어주세요",file_types=[".docx"], file_count="single")
            compare_upload_button.upload(upload_file, compare_upload_button, file2_output)
            # pdb.set_trace()
        with gr.Group():
            with gr.Column():
                result_output = gr.File()
                start_button = gr.Button('비교시작')
                start_button.click(backend_test.test_fn, inputs=[file1_output,file2_output], outputs = result_output)
                # start_button.click(fn = backend_test.test_fn,inputs=[file1_output,file2_output],outputs=result_output)

                # start_button.click(fn=upload_file, input=[file1_output,file2_output], output=result_output)


demo.launch(share=True)
# https://www.gradio.app/guides/blocks-and-event-listeners -> 이거보고 수정하기


















# def upload_file(file1,file2):
#     file1_paths = [file.name for file in file1]
#     file2_paths = [file.name for file in file2]

#     return file1_paths # 고쳐야할 부분(임의로 1개 바로 return하게 해놓았음)

# with gr.Blocks() as demo:
#     with gr.Row():
#         file_orgin = gr.File(label="원본파일 입력",file_count="single", file_types=['.docx'])
#         file_compare = gr.File(label="비교 파일 입력", file_count="single", file_types=['.docx'])
#     with gr.Row():
#         text_output = gr.File(label="결과 파일",file_count="single",file_types=[".docx"])
#         # text_output2 = gr.File(label="결과 파일",file_count="single",file_types=[".docx"])
#     with gr.Row():
#         compare_start_button = gr.Button("비교 시작")
#         compare_start_button.click(upload_file,inputs=[file_orgin,file_compare],outputs=text_output)

    
# 돌렸을때 오류뜨는거 잡기(pdb사용)
# text_output은 왜  file_orgin,file_compare처럼 안뜨는지 원인찾기 
    

    
demo.launch(share=True)