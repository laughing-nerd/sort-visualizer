import time
import visualizer

def sort(arr, SCREEN_WIDTH, SCREEN_HEIGHT):
        n=len(arr)

        screen, clock = visualizer.initiate_screen(SCREEN_WIDTH, SCREEN_HEIGHT, 'Insertion Sort')
        w = SCREEN_WIDTH / ((2*n)+1)
        addVal=0

        start1 = time.process_time()
        for i in range(1, n):
            index = i
            while index>0:

                start2 = time.process_time()
                visualizer.plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, index)
                end2=time.process_time()
                addVal+=(end2-start2)

                if(arr[index]<arr[index-1]):
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                index-=1
        
        end1 = time.process_time()
        # print((end1-start1)-addVal)

        visualizer.plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, index)