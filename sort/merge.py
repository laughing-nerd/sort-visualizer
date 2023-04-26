import time
import visualizer

def sort(arr, SCREEN_WIDTH, SCREEN_HEIGHT):
    n = len(arr)

    screen, clock = visualizer.initiate_screen(SCREEN_WIDTH, SCREEN_HEIGHT, 'Insertion Sort')
    w = SCREEN_WIDTH / ((2*n)+1)
    addVal=0
    i = 1

    start1 = time.process_time()
    while i < n:
        for j in range(0, n, 2*i):

            left = arr[j:j+i]
            right = arr[j+i:j+2*i]
            merged = []

            left_count=j
            right_count=j+1
            while left and right:

                start2 = time.process_time()
                visualizer.plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, left_count, right_count)
                end2 = time.process_time()
                addVal+=(end2-start2)

                if left[0] < right[0]:
                    left_count+=1
                    merged.append(left.pop(0))
                else:
                    right_count+=1
                    merged.append(right.pop(0))
                

            merged += left + right
            start3 = time.process_time()
            for k in range(len(merged)):
                visualizer.plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, k)
            end3 = time.process_time()
            addVal+=(end3-end1)
            arr[j:j+len(merged)] = merged
        i *= 2
    end1 = time.process_time()

    # print((end1-start1)-addVal)
    visualizer.plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, 0)


