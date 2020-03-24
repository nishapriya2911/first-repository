from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('input.html')

@app.route('/selection_sort', methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = int(request.form['n'])
        num2 = request.form['num']
        arr=[]
        x=num2.split()
        for i in x:
            arr.append(int(i))
        for j in range(num1):
            ind=j
            for k in range(j+1,num1):
                if arr[ind]>arr[k]:
                 ind=k
            temp=arr[j]
            arr[j]=arr[ind]
            arr[ind]=temp
        return render_template('output.html',array=arr,n=num1)
