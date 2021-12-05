from sys import exec_prefix
import tkinter
import tkinter.ttk
from math import *

window = tkinter.Tk()
window.title("MST Algorithm")
window.geometry("900x800+100+100")  # 윈도우 사이즈 (900x800), 윈도우 시작 위치 (100,100)
window.resizable(False, False)  # 윈도우 크기 변경 불가능

node_number = 0
node = [] # 노드의 좌표값
node_V = [] # 전체 노드를 행렬로 표현(가중치 표기)

def drawingNode(event):
  global node_number
  node_number += 1
  x = event.x
  y = event.y
  main_canvas.create_oval(x-13,y-13, x+13, y+13, fill="skyblue", width=0)
  main_canvas.create_text(x, y, text=str(node_number))
  node.append([x,y])
  # 그려진 노드를 출발지, 목적지 노드 콤보박스로 넣기
  start_node['value'] = [v for v in range(1, node_number+1)]
  end_node['value'] = [v for v in range(1, node_number+1)]
  # 노드의 가중치 배열 크기 늘리기
  node_V.append([0 for i in range(len(node_V)+1)])
  for i in range(len(node_V)-1):
    node_V[i] += [0]

  print("node_V : ", node_V)


def drawingEdge(event, start, end, weight):
  s_x = node[int(start)-1][0]
  s_y = node[int(start)-1][1]
  e_x = node[int(end)-1][0]
  e_y = node[int(end)-1][1]
  w_x, w_y = drawingWeight(s_x, s_y, e_x, e_y)
  # 간선과 가중치 그리기
  main_canvas.create_line(s_x, s_y, e_x, e_y, fill="black")
  main_canvas.create_text(w_x, w_y, text=weight, fill="blue")
  # 노드의 가중치 배열에 가중치 넣기
  node_V[int(start)-1][int(end)-1] = weight
  node_V[int(end)-1][int(start)-1] = weight

  print("node_V, Edge :", node_V)


def drawingWeight(s_x, s_y, e_x, e_y):
  if s_x > e_x:
    mid_x = (s_x - e_x) / 2 + e_x
  else:
    mid_x = (e_x - s_x) / 2 + s_x

  if s_y > e_y:
    mid_y = (s_y - e_y) / 2 + e_y
  else:
    mid_y = (e_y - s_y) / 2 + s_y

  return (mid_x, mid_y)


# 프레임 설정
# frame1
frame1=tkinter.Frame(window, relief="solid", bd=1)
frame1.place(x=0, y=0, width=450, height=400)

# frame2
frame2=tkinter.Frame(window, relief="solid", bd=1)
frame2.place(x=450, y=0, width=450, height=400)

# frame3
frame3=tkinter.Frame(window, relief="solid", bd=1)
frame3.place(x=0, y=400, width=450, height=400)

# frame4
frame4=tkinter.Frame(window, relief="solid", bd=1)
frame4.place(x=450, y=400, width=450, height=400)

##################################################################

### 프레임 내부
button1=tkinter.Button(frame1, text="프레임1")
button1.pack(anchor="center")

## frame1 캔버스
main_canvas=tkinter.Canvas(frame1, bd=2)
main_canvas.place(x=0, y=0, width=450, height=400)
main_canvas.bind("<Button-1>", drawingNode)

## frame2
label2=tkinter.Label(frame2, width=5, height=3)
label2.pack()

# 가중치 적용
labelframe_weight=tkinter.LabelFrame(frame2, text="가중치 적용")
labelframe_weight.pack()

start_node=tkinter.ttk.Combobox(labelframe_weight, width=10, values=[])
start_node.pack()
start_node.set("출발지")

end_node=tkinter.ttk.Combobox(labelframe_weight, width=10, values=[])
end_node.pack()
end_node.set("목적지")

entry = tkinter.Entry(labelframe_weight)
entry.pack()

weight_btn = tkinter.Button(labelframe_weight, text="적용하기", overrelief="solid", width=5, 
                                    command=lambda: drawingEdge(e, start_node.get(), end_node.get(), entry.get()),
                                    repeatdelay=1000, repeatinterval=100)
weight_btn.pack()


# 결과 확인
labelframe=tkinter.LabelFrame(frame2, text="결과 확인!")
labelframe.pack()

mid_result=tkinter.Button(labelframe, text="중간 결과")
mid_result.pack(side="left")
final_result=tkinter.Button(labelframe, text="최종 결과")
final_result.pack(side="right")

## frame3
prim_canvas=tkinter.Canvas(frame3, bd=2)
prim_canvas.place(x=0, y=0, width=450, height=400)
# prim_canvas.bind("<Button-1>", drawingNode)

## frame4
kruskal_canvas=tkinter.Canvas(frame4, bd=2)
kruskal_canvas.place(x=0, y=0, width=450, height=400)
# kruskal_canvas.bind("<Button-1>", drawingNode)

window.mainloop()
