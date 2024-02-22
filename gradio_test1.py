import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")
    
if __name__ == "__main__":
    demo.launch(share=True)
    # demo.launch(server_name="0.0.0.0", server_port=8000) # 이렇게 하니 접속안된다(나중에 알아봐야할듯)

