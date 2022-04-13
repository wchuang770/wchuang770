from crypt import methods
from turtle import textinput
from flask import Flask,request,render_template,url_for
import os

app = Flask(__name__)

# 文件输入并保存
@app.route('/text_input' , methods = ['POST','GET'])
def text_input():
   if request.method == 'POST':
      beforetext = request.form['textinput']
      with open('/static/textfile.txt' , 'w' , encoding='utf-8') as f:
         f.write(beforetext)
         f.close
   else:
      beforetext = request.args.get('textinput')
      with open('/static/textfile.txt' , 'w' , encoding='utf-8') as f:
         f.write(beforetext)
         f.close
   return 

# 文件上传
@app.route('/file_upload' , methods=["POST","GET"])
def file_upload():
   file = request.files.get("filename")
   if file is None:
      return {
         'message':"文件上传失败"
      }
   file_name = file.filename.replace(" ","")
   print("获取上传的文件名称为[%s]\n % file_name")
   file.save(os.path.dirname(__file__)+'/static/'+file_name)
   return {
      'code':200,
      'message':"文件上传成功",
      'filename': file_name,
   }
   a='1'
   return render_template('main.html',a=a)


if __name__ == '__main__':
   app.run()
