def moveDisc(discCnt, fromBar, toBar, viaBar):
    if discCnt == 1:
        print(f"{discCnt}disc를:{fromBar} 에사 {toBar}(으)로 이동 ")

    else:
        #discCnt-1 개들을 경유 기둥으로 이동
        moveDisc(discCnt - 1, fromBar, viaBar, toBar)

        #discCnt 를 목적 기둥으로 이동
        print(f"{discCnt}disc를:{fromBar} 에사 {toBar}(으)로 이동! ")

        #discNo-1 개들을 도착 기둥으로 이동
        moveDisc(discCnt -1, viaBar, toBar, fromBar)


moveDisc(3, 1, 3, 2)
