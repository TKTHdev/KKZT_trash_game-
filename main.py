import pyxel

score=0
life=3
count=0
tama=True

class TaxMoney:
    def __init__(self):
        self.id = pyxel.rndi(0, 3)
        self.x = 200
        self.y = 35
        self.speed = 2
        self.hit = False

    def move(self):
        if not self.hit:
            self.x -= self.speed
        else:
            self.x -= self.speed/2
            self.y += self.speed

TaxMoneyList=[]

class Bullet:
    def __init__(self,dirx,diry):
        self.speed = 3
        self.x = 30
        self.y = 160
        self.dx = dirx
        self.dy = diry
    def move(self):
        self.x +=11*self.dx/(self.dx+self.dy)
        self.y -=11*self.dy/(self.dx+self.dy)

BulletList = []

class Game:
    global score,life,count,tama
    def __init__(self):

        pyxel.init(200,200,fps=60)
        pyxel.load("assets/charactor.pyxres")
        pyxel.run(self.update, self.draw)

        pyxel.x = pyxel.mouse_x
        pyxel.y = pyxel.mouse_y
        self.tama = True




    def update(self):
        global score,life,count
        count+=1
        if count%60==0:
            TaxMoneyList.append(TaxMoney())

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_A):
            TaxMoneyList.append(TaxMoney())

        if pyxel.btnp(pyxel.KEY_SPACE):
            BulletList.append(Bullet(abs(pyxel.mouse_x-30),abs(pyxel.mouse_y-160)))

        for money in TaxMoneyList:
            money.move()
            if money.x < 0:
                TaxMoneyList.remove(money)

            if money.x>75 and money.x<107 and money.y>170 and money.y<200 and money.id==0:
                TaxMoneyList.remove(money)
                score += 1
            if money.x>75 and money.x<107 and money.y>170 and money.y<200 and money.id==1:
                TaxMoneyList.remove(money)
                score -= 1

            if money.x>5 and money.x<25 and money.y>170 and money.y<200 and money.id==1:
                TaxMoneyList.remove(money)
                life -= 1


            for bullet in BulletList:
                if bullet.x< money.x + 5 and bullet.x > money.x - 5 and bullet.y < money.y + 5 and bullet.y > money.y - 5:
                    money.hit = True
                    BulletList.remove(bullet)

        for bullet in BulletList:
            bullet.move()
            if bullet.x > 200 or bullet.y< 0:
                BulletList.remove(bullet)


    def draw(self):
        global tama,count
        pyxel.cls(6)
        pyxel.blt(20,20,0,0,80,18,15,5)
        pyxel.blt(70,60,0,0,80,18,15,5)
        pyxel.blt(40,40,0,0,80,18,15,5)
        pyxel.blt(120,30,0,0,80,18,15,5)
        pyxel.blt(190,30,0,24,80,15,15,5)
        pyxel.blt(130,60,0,24,80,15,15,5)

        pyxel.circ(200,0,30,8)


        pyxel.text(5, 5, "Press Q to quit", 0)



        if count%20==0:
            if tama:
                tama=False
            else:
                tama=True

        if tama:
            pyxel.blt(160,170,0,0,96,20,40,5)
        else:
            pyxel.blt(160,170,0,0,128,20,40,5)



        for bullet in BulletList:
            pyxel.circ(bullet.x, bullet.y, 2, 1)



        pyxel.blt(5,170,0,0,0,20,30,5)
        pyxel.blt(50,170,0,0,32,30,40,5)

        for money in TaxMoneyList:
            if money.id==0:
                pyxel.blt(money.x-5,money.y-5,0,0,64,15,15,5)
                if not money.hit:
                    pyxel.line(money.x+3,money.y,money.x+3,money.y-23,0)
            else:
                pyxel.blt(money.x-5,money.y-5,0,16,64,15,15,5)
                if not money.hit:
                    pyxel.line(money.x+3,money.y,money.x+3,money.y-23,1)

        pyxel.line(20,180,pyxel.mouse_x,pyxel.mouse_y,3)

        pyxel.line(0,12,200,12,0)

        pyxel.text(5, 15, "Score: " + str(score), 0)


Game()
