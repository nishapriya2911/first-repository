from flask import Flask, render_template, request
import sys
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('input.html')

def egg(n,f):
    ans=0
    if (f==1 or f==0):
        return f
    if (n==1):
        return f
    m=sys.maxsize
    for x in range(1,f+1):
        res=max(egg(n-1,x-1),egg(n,f-x))
        if (res<m):
            m=res
    return m+1

@app.route('/egg_drop', methods=['POST'])
def send():
    if request.method == 'POST':
        n = int(request.form['n'])
        f = int(request.form['f'])
        ans=egg(n,f)
        return render_template('output.html',n=n,f=f,ans=int(ans))
