paper_a5 = 3366;
% paper_a7 = 3772;
% paper_a8 = 1994;
% paper_a10 = 5062;
paper_a11 = 10573;
papers = [paper_a5 ;  paper_a11];
total_papers = paper_a5 + paper_a11 ; 

G = zeros(2);
for i =1 : 2
    for j=1:2
        if i==j
            G(i,j) = 0;
        else
            G(i,j)= (papers(i)+papers(j))/total_papers ;
        end
    end
end
g =2; %number of domains


%{
Implementation of CROSSRANK Algorithm

G: the adjacency matrix of main network
A: domain specific networks A = { A1,...,Ag}
Ai: the ith domain specific network
theta: the one-to-one mapping function
R := <G,A,theta>, networks of networks
ri: the ranking vector of Ai
ei: the ith query vector for Ai
In: an n*n identity matrix
Iij: the set of common nodes between Ai and Aj
dm(i): the degree matrix: Dm = diag(dm(1),...,dm(g))
g: the number of nodes in main network
ni: the number of nodes in Ai, (i=1,....,g)
mi: the number of edges in Ai, (i=1,....,g)
c,a: the paramerters 0<c<1, and a>0

DONE
Tested A_cap

TODO
Calculate D_o
Test Y_cap
Test the online computation part of the algorithm

%}

%function r = crossrank( G, g, A, n, r, e, a, c)

% Construct A-cap and Y-cap from R.


% ID's for each domain
ID_1= cell(g);
ID_1{1}= A5_ID';% ids for domain 1
% ID_1{2}= A7_ID'; % ids for domain 2
% ID_1{3}= A8_ID'; % ids for domain 3
% ID_1{4}= A10_ID'; % ids for domain 10
ID_1{2}= A11_ID'; % ids for domain 11
ID = ID_1{1}';
for i=2:g
    Temp = ID_1{i}';
    for j=1:size(Temp,1)
        ID = [ID;Temp(j,1)];
    end
end
ID = ID';
% % Domain Matrices
% A1 = [ 0     15  0   0   10
%        15    0   6   0   0
%        0     6   0   2   0
%        0     0   2   0   1
%        10    0   0   1   0
%      ];
% A2 = [ 0    12  0   14
%        12   0   7   0
%        0    7   0   5
%        14   0   5   0
%      ];
% A3 = [ 0    17  20
%        17   0   6
%        20   6   0
%       ];
 
 A = {A5,A11};

 dm = zeros(g,1);
for i=1:g
    for j=1:g
        if i~=j
            dm(i) = dm(i) + 1;
        end
    end
end
dm = dm'

% Calculation of A_cap
A_out = A;
for i = 1:size(A,2)
    X = A{i};
    D = eye(length(X));
    for y = 1:size(X,1)
        sum = 0;
        for z = 1:size(X,1)
            sum = sum + X(y,z);
        end
        if sum==0
            sum=0.01;
        end
        D(y,y) = sum;
    end
    D_sqrt= sqrtm(D);
    A_out{i} =  inv(D_sqrt)*X*inv(D_sqrt);  %#ok<MINV>
    A_out{i}
end

A_cap=[];
for i=1:g
    A_cap = blkdiag(A_cap,A_out{i});
end

% Calcuation of O
O_size =0;

for i=1:g
    O_size=O_size+size(A{i},1);
end
O = zeros(O_size);

A_size= [];
for i=1:g
    if i==1
        A_size = [A_size;size(A{i},1)];
    else
        temp = A_size(i-1,1);
        A_size = [A_size;size(A{i},1)+temp];
    end
end

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

% Calculation of Degree Matrix D_o
D_o = eye(length(O));
for y = 1:size(O,1)
  sum = 0;
  for z = 1:size(O,1)
      sum = sum + O(y,z);
  end
  D_o(y,y) = sum;
end

% Calculation of Degree Matric D_t
for i = 1:g
    I_n = eye(size(A{i},1));
    D_t_out{i} = dm(i)*I_n;
end

D_t =[];
for i=1:g
    D_t = blkdiag(D_t,D_t_out{i});
end

D_t = D_t - D_o;
Y = O + D_t;

D_y = eye(length(Y));
for y = 1:size(Y,1)
    sum = 0;
    for z = 1:size(Y,1)
        sum = sum + Y(y,z);
    end
    D_y(y,y) = sum;
end
D_y_sqrt= sqrtm(D_y);
Y_cap =  inv(D_y_sqrt)*Y*inv(D_y_sqrt);  %#ok<MINV>

size1 = size(A5_ID,1);
size2 = size(A11_ID,1);

e1 = ones(1,size1);
e2 = ones(1,size2);
e1 = e1 * (1/size1);
e2 = e2 * (1/size2);

e = {e1,e2};
e_new = [];    
for m = 1:size(e,2)
    e_new = horzcat(e_new,e{m});
end
e_new = transpose(e_new);

r_old = zeros(size(e_new,1),1);
r_new = e_new;

c=0.85;
a=0.5;
%while ~isequal(r_new,r_old)
for i=1:1000   
    i
    r_old = r_new;
    r_new = ((c/(1+2*a))*A_cap + (2*a/(1+2*a))*Y_cap)*r_new + ((1-c)/(1+2*a))*e_new;
    
end

r_new


%end
% ID_1= cell(g);
% ID_1{1}= [ 1 5  4  3  2]; % ids for domain 1
% ID_1{2}= [ 1  6  8  7]; % ids for domain 2
% ID_1{3}= [ 1 10 9]; % ids for domain 3
% ID = ID_1{1}';
% for i=2:g
%     Temp = ID_1{i}';
%     for j=1:size(Temp,1)
%         ID = [ID;Temp(j,1)];
%     end
% end
% ID = ID';
% 
% A1 = [ 0     15  0   0   10
%        15    0   6   0   0
%        0     6   0   2   0
%        0     0   2   0   1
%        10    0   0   1   0
%      ];
% A2 = [ 0    12  0   14
%        12   0   7   0
%        0    7   0   5
%        14   0   5   0
%      ];
% A3 = [ 0    17  20
%        17   0   6
%        20   6   0
%       ];
% A = {A1,A2,A3};
% 
% O_size =0;
% for i=1:g
%     O_size=O_size+size(A{i},1);
% end
% O = zeros(O_size);
% A_size= [ ];
% for i=1:g
%     if i==1
%         A_size = [A_size;size(A{i},1)];
%     else
%         temp = A_size(i-1,1);
%         A_size = [A_size;size(A{i},1)+temp];
%     end
% end
% 
% for i=1:O_size
%     for j=1:O_size
%         if ID(i)== ID(j)
%             O(i,j)=1;
%         end
%     end
% end
% for i=1:g
%     for j=1:g
%         if i==1 && j==1
%            O(1:A_size(i,1),1:A_size(j,1))= G(i,j)*O(1:A_size(i,1),1:A_size(j,1)); 
%         elseif i==1 && j~=1
%            O(1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1))= G(i,j)*O(1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1));
%         elseif i~=1 && j==1
%            O(A_size(i-1,1)+1:A_size(i,1),1:A_size(j,1))= G(i,j)*O(A_size(i-1,1)+1:A_size(i,1),1:A_size(j,1));
%         else
%            O(A_size(i-1,1)+1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1))= G(i,j)*O(A_size(i-1,1)+1:A_size(i,1),A_size(j-1,1)+1:A_size(j,1));
%         end
%     end
% end
