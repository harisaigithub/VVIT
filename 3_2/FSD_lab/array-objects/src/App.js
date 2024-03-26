import React from 'react';
import TableView from './TableView';
import './index.css';

const App = () => {
  const data = [
    {ID : 1 , Name : 'HARI' ,   Age : 20},
    {ID : 2 , Name : 'soCHOa'   ,   Age : 21},
    {ID : 3 , Name : 'sonu' ,   Age : 20},
    {ID : 4 , Name : 'ankitha' ,   Age : 21},
    {ID : 5 , Name : 'kanae'  ,   Age : 21},

  ];

  return (
    <div>
      <h1 style = {{ textAlign : 'center' , borderBottom : '2px solid blue' , paddingTop : '20px',marginBottom : '100px'}}>
        Array of Objects - TableView
      </h1>
      <TableView data= {data} />
    </div>
  );
};

export default App;
