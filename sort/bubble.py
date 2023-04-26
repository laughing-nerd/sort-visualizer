import time
import visualizer

def sort(arr, SCREEN_WIDTH, SCREEN_HEIGHT):
    n=len(arr)

    screen, clock = visualizer.initiate_screen(SCREEN_WIDTH, SCREEN_HEIGHT, 'Bubble Sort')
    w = SCREEN_WIDTH / ((2*n)+1)
    addVal=0

    start1 = time.process_time()
    for i in range(0,n-1):
        for j in range(0,n-i-1):

            start2 = time.process_time()
            visualizer.plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, j)
            end2=time.process_time()
            addVal+=(end2-start2)
            
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j] #Swapping elements
    end1 = time.process_time()
    # print((end1-start1)-addVal)

    visualizer.plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, j)
