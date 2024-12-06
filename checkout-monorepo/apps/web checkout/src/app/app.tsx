import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from '../pages/landing-page';
import ProductPage from '../pages/product-page';


const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Define the routes here */}
          <Route path="/" element={<LandingPage />} />
          <Route path="/product/:id" element={<ProductPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
