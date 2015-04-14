%Set preferences with setdbprefs.
setdbprefs('DataReturnFormat', 'cellarray');
setdbprefs('NullNumberRead', 'NaN');
setdbprefs('NullStringRead', 'null');


%Make connection to database.  Note that the password has been omitted.
%Using ODBC driver.
conn = database('mysqlSWM', 'root', '');

%Read data from database.
curs = exec(conn, 'SELECT  * FROM coauthor WHERE domain_key=5');

curs = fetch(curs);
close(curs);

%Assign data to output variable
Coauthor_cell = curs.Data;
Coauthor = cell2mat(Coauthor_cell);
x=size(Coauthor,1);


% cmd = 'SELECT count(distinct(coauthor.author_key1)) FROM coauthor where coauthor.domain_key=11';
% %Read data from database.
% curs = exec(conn, cmd);
% 
% curs = fetch(curs);
% close(curs);
% 
% %Assign data to output variable
% Domain_author_count = curs.Data;
% DA_count = cell2mat(Domain_author_count);
% %create a matrix of size DA_count initialized to zero




%Read data from database.
curs = exec(conn, 'SELECT coauthor.author_key1 FROM coauthor where coauthor.domain_key=5');

curs = fetch(curs);
close(curs);


%Assign data to output variable
Dist_Author_ID1 = curs.Data;
A5_ID1 = cell2mat(Dist_Author_ID1);

%Read data from database.
curs = exec(conn, 'SELECT coauthor.author_key2 FROM coauthor where coauthor.domain_key=5');

curs = fetch(curs);
close(curs);


%Assign data to output variable
Dist_Author_ID2 = curs.Data;
A5_ID2 = cell2mat(Dist_Author_ID2);

A5_ID = horzcat(A5_ID1',A5_ID2');
A5_ID = A5_ID';


A5_ID = unique(A5_ID);

[m,n] = size(A5_ID);

A5_ID = sort(A5_ID);
A5= zeros(m);
for i=1:x
    Author1 = Coauthor(i,2);
    Author2 = Coauthor(i,3);
    a = find(A5_ID == Author1);
    b = find(A5_ID == Author2);
    if ~isempty(b)
       A5(a,b) = Coauthor(i,4);
       A5(b,a) = Coauthor(i,4); 
    end
    
end








% A4(5661,18820)
%calculating A - adjacency matrix for a domain
% 
% for i=1:DA_count
%     for j=i+1:DA_count
%         i
%         j
%         a_key1 = int2str(A3_ID(i));
%         a_key2 = int2str(A3_ID(j));
%         if i==j
%             A4(i,j)=0;
%         else
%             %Read data from database.
%             cmd_coauthor = 'SELECT coauthor.coauthor_count FROM coauthor where coauthor.domain_key=3 and coauthor.author_key1=';
%             cmd_coauthor = strcat(cmd_coauthor,a_key1);
%             cmd_coauthor = strcat(cmd_coauthor,' and author_key2=');
%             cmd_coauthor = strcat(cmd_coauthor,a_key2);
%             curs = exec(conn, cmd_coauthor);
% 
%             curs = fetch(curs);
%             close(curs);
%             
%             %Assign data to output variable
%             coauthor_cell = curs.Data;
%             coauthor = cell2mat(coauthor_cell);
%             
%             
%             if strcmp(coauthor_cell,'No Data')
%                 A4(i,j) = 0;
%                 A4(j,i) = 0;
%             else   
% %                     if coauthor~=0
% %                     cmd_coauthor
% %                     coauthor
% %                     end
%                 A4(i,j) = coauthor;
%                 A4(j,i) = coauthor;
%             end
%         end
%     end
% end

fprintf('Execution completed \n');
%Close database connection.
close(conn);

%Clear variables
clear curs conn

for i=1:m
    sum=0;
    for j=1:m
        sum = sum + A5(i,j);
        %fprintf('%d %d   ',sum,A5(i,j))
    end
   % fprintf('\n')
    if(sum==0)
        fprintf('%d ',i)
    end
end
fprintf('Execution completed \n');