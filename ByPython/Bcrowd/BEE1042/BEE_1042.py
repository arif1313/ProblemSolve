
# x=int(input());
# y=int(input());
# z=int(input());
# orginal=[x,y,z];
# shorted_li=sorted(orginal);


# for item in shorted_li:
#     print(item);
# print();

# for item in orginal:
#     print(item);

a, b, c = map(int, input().split())
orginal =[a,b,c]

sorted_seq=sorted(orginal);

for item in sorted_seq:
    print(item);
print();
for item in orginal:
    print(item);
