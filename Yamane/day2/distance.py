import sys
args=sys.argv
input1=args[1]
input2=args[2]
station={"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}
distance=abs(station[input1]-station[input2])
print(distance,end="")