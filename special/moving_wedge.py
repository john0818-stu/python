# Morris H. 11/19

from vpython import *

#初始條件輸入

while True:
    theta = int(input('Please enter theta(degree) >>> '))
    if theta > 0 and theta < 90:
        break
    else:
        print('Please enter the value between 0 to 90')
theta *= pi/180
print('Minimum cofficient for ball to stay still = ', tan(theta))
k = float(input('Please enter coefficient of friction >>> '))
# M = int(input('Please enter mass of Big Block >>> '))
# m = int(input('Please enter mass of Small Block >>> '))


# 初始值設定

M, m = 10, 6
g = 9.8

# 物體運動公式

#當摩擦係數大於tan斜坡角度時，物體不會運動

if k >= tan(theta):
    a_m, a_M, m_a_x, m_a_y, M_a_x = 0, 0, 0, 0, 0
else:
    a_m = g/(M*(cos(theta)**2 + k*sin(theta)*cos(theta))/(m + M)/(sin(theta) - k*cos(theta))+ sin(theta))
    a_M = m*cos(theta)/(m+M)*a_m

    m_a_x = a_m*cos(theta)-a_M
    m_a_y = -a_m*sin(theta)
    M_a_x = -a_M


# 場景設定

scene = canvas(title='Moving Block', width=1600, height=1000, align='left')
scene.camera.pos = vec(10, 13, 40)
scene.camera.axis = vec(-5, -13, -30)

# 大木塊

A = vertex(pos=vec(0, 0, 0), color=color.cyan, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))
B = vertex(pos=vec(10/tan(theta), 0, 0), color=color.green, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))
C = vertex(pos=vec(10/tan(theta), 0, 10), color=color.green, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))
D = vertex(pos=vec(0, 0, 10), color=color.cyan, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))
E = vertex(pos=vec(0, 10, 10), color=color.cyan, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))
F = vertex(pos=vec(0, 10, 0), color=color.cyan, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))

T1 = triangle(v0=E, v1=D, v2=C)
T2 = triangle(v0=F, v1=A, v2=B)
Q1 = quad(v0=F, v1=E, v2=D, v3=A)
Q2 = quad(v0=F, v1=E, v2=C, v3=B)
Q3 = quad(v0=A, v1=B, v2=C, v3=D)

#地板

floor = box(pos=vec(0,0,0), size=vec(300, 1, 30), color=color.blue, v=vec(0, 0, 0), a=vec(0, 0, 0))

# 小球

ball = sphere(pos=vec(1.5/sin(theta), 10, 5), radius=1.5, v=vec(0, 0, 0),
             a=vec(m_a_x, m_a_y, 0), texture=textures.wood, up=vec(sin(theta), cos(theta), 0))

# 作圖

g1 = graph(title='Momentum (x direction)', xtitle='time', ytitle='P', align='right', 
           width=1000, height=500)
g2 = graph(title='Total Energy', xtitle='time', ytitle='E', align='right', 
           width=1000, height=500)

# 動量

total_p = gdots(graph=g1, color=color.blue)
m_p = gdots(graph=g1, color=color.cyan)
M_p = gdots(graph=g1, color=color.green)


# 能量

m_E = gdots(graph=g2, color=color.blue)
M_E = gdots(graph=g2, color=color.cyan)
total_E = gdots(graph=g2, color=color.green)

#運動動畫

dt = 0.01
t = 0

while ball.pos.x < 30 or t > 10:
#while ball.pos.x < 20 or t > 10:

    rate(50)

    # 小木塊移動

    ball.v.x += ball.a.x * dt
    ball.pos.x += ball.v.x * dt
    ball.v.y += ball.a.y * dt
    ball.pos.y += ball.v.y * dt

    # 大木塊移動

    A.v.x += A.a.x * dt
    A.pos.x += A.v.x * dt
    B.v.x += B.a.x * dt
    B.pos.x += B.v.x * dt
    C.v.x += C.a.x * dt
    C.pos.x += C.v.x * dt
    D.v.x += D.a.x * dt
    D.pos.x += D.v.x * dt
    E.v.x += E.a.x * dt
    E.pos.x += E.v.x * dt
    F.v.x += F.a.x * dt
    F.pos.x += F.v.x * dt

    # 當木塊到底

    if ball.pos.y <= ball.radius+floor.size.y/2:
        ball.v.x = (ball.v.x**2 + ball.v.y**2)**0.5
        ball.a.x, ball.a.y, ball.v.y = 0, 0, 0
        ball.up = vec(0, 1, 0)
        A.a.x, B.a.x, C.a.x, D.a.x, E.a.x, F.a.x = 0, 0, 0, 0, 0, 0
        ball.pos.x += ball.v.x * dt
        A.pos.x += A.v.x * dt
        B.pos.x += B.v.x * dt
        C.pos.x += C.v.x * dt
        D.pos.x += D.v.x * dt
        E.pos.x += E.v.x * dt
        F.pos.x += F.v.x * dt

    # 作圖(動量和能量)
    # 到達底部後不畫動量

    if ball.pos.y >= ball.radius+floor.size.y/2:
        p = ball.v.x * m + A.v.x * M
        total_p.plot(pos=(t, p))
        m_p.plot(pos=(t, m * ball.v.x))
        M_p.plot(pos=(t, M * A.v.x))

    K = 0.5*m*(ball.v.x**2 + ball.v.y**2) + 0.5*M*A.v.x**2
    U = m*g*(ball.pos.y - (ball.radius+floor.size.y/2))

    m_E.plot(pos=(t, K))
    M_E.plot(pos=(t, U))

    total_E.plot(pos=(t, K+U))

    t += dt
