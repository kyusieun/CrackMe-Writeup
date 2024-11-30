HDD를 CD-Rom으로 인식시키기 위해서는 GetDriveTypeA의 리턴값이 무엇이 되어야 하는가

![success](./success.png)

풀이
0x401024에서 cmp eax, esi에 브레이크 포인트를 걸고 ESI를 EAX값인 1로 수정