// frontend/src/components/common/Card.jsx
import React from 'react';

export const Card = ({ 
  children, 
  className = '', 
  padding = 'p-6',
  hover = false,
  ...props 
}) => {
  return (
    <div 
      className={`
        bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700
        ${hover ? 'hover:shadow-md transition-shadow duration-200' : ''}
        ${padding} ${className}
      `}
      {...props}
    >
      {children}
    </div>
  );
};