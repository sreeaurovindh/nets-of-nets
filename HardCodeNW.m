
g =3; %number of domains
G = [ 0     0.6     0 
      0.6   0       0.4
      0     0.4     0
    ];

ID_1= cell(g);
ID_1{1}= [ 1 5  4  3  2]; % ids for domain 1
ID_1{2}= [ 1  6  8  7]; % ids for domain 2
ID_1{3}= [ 1 10 9]; % ids for domain 3
ID = ID_1{1}';
for i=2:g
    Temp = ID_1{i}';
    for j=1:size(Temp,1)
        ID = [ID;Temp(j,1)];
    end
end
ID = ID';

A1 = [ 0     15  0   0   10
       15    0   6   0   0
       0     6   0   2   0
       0     0   2   0   1
       10    0   0   1   0
     ];
A2 = [ 0    12  0   14
       12   0   7   0
       0    7   0   5
       14   0   5   0
     ];
A3 = [ 0    17  20
       17   0   6
       20   6   0
      ];
A = {A1,A2,A3};

O_size =0;
for i=1:g
    O_size=O_size+size(A{i},1);
end
O = zeros(O_size);
A_size= [ ];
for i=1:g
    if i==1
        A_size = [A_size;size(A{i},1)];
    else
        temp = A_size(i-1,1);
        A_size = [A_size;size(A{i},1)+temp];
    end
end
A_size

for i=1:O_size
    for j=1:O_size
        if ID(i)== ID(j)
            O(i,j)=1;
        end
    end
end
for i=1:g
    for j=1:g
        if i==1 && j==1
           O(1:A_size(i,1),1:A_size(j,1))= G(i,j)*O(1:A_size(i,1),1:A_size(j,1)); 
        elseif i==1 && j~=1
           O(1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1))= G(i,j)*O(1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1));
        elseif i~=1 && j==1
           O(A_size(i-1,1)+1:A_size(i,1),1:A_size(j,1))= G(i,j)*O(A_size(i-1,1)+1:A_size(i,1),1:A_size(j,1));
        else
           O(A_size(i-1,1)+1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1))= G(i,j)*O(A_size(i-1,1)+1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1));
        end
    end
end
O