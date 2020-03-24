from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('input.html')

@app.route('/insertion_sort', methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = int(request.form['n'])
        num2 = request.form['num']
        arr=[]
        x=num2.split()
        for i in x:
            arr.append(int(i))
        for j in range(1,num1):
            key=arr[j]
            k=j-1
            while k>=0 and key<arr[k]:
                arr[k+1]=arr[k]
                k-=1
            arr[k+1]=key
        return render_template('output.html',array=arr,n=num1)
