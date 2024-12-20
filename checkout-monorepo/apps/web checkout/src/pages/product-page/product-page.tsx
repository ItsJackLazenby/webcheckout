import React from 'react';
import { useParams } from 'react-router-dom';

const ProductPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();

  return (
    <div>
      <h1>Product Details</h1>
      <p>Displaying details for product ID: {id}</p>
    </div>
  );
};

export default ProductPage;
