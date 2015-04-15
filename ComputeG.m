%Set preferences with setdbprefs.
setdbprefs('DataReturnFormat', 'cellarray');
setdbprefs('NullNumberRead', 'NaN');
setdbprefs('NullStringRead', 'null');


%Make connection to database.  Note that the password has been omitted.
%Using ODBC driver.
conn = database('SWM1', 'root', '');
g=11;
arr=[];
for i=2:g
    %Read data from database.
    q= 'SELECT 	count(*) FROM swm_dataset1.paper_details where domain_key =';
    iStr=int2str(i);
    query= strcat(q,iStr);
    curs = exec(conn, query);

    curs = fetch(curs);
    close(curs);

    %Assign data to output variable
    untitled = curs.Data;
    arr=[arr;untitled];
end
totalPaperCount=127626;
arr=cell2mat(arr);
%Close database connection.
close(conn);
G=zeros(10);
for i=1:10
    for j=1:10
        if i ==j
            G(i,j)=0;
        else
            G(i,j)=(arr(i)+arr(j))/totalPaperCount;
        end
    end
end
G
%Clear variables
clear curs conn