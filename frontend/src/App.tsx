import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Navbar from './components/layout/Navbar';
import Dashboard from './pages/Dashboard';
import HealthRecord from './pages/HealthRecord';
import RiskAssessment from './pages/RiskAssessment';
import InsurancePolicies from './pages/InsurancePolicies';
import Login from './pages/Login';
import Register from './pages/Register';
import PrivateRoute from './components/auth/PrivateRoute';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route
              path="/"
              element={
                <PrivateRoute>
                  <Dashboard />
                </PrivateRoute>
              }
            />
            <Route
              path="/health-record"
              element={
                <PrivateRoute>
                  <HealthRecord />
                </PrivateRoute>
              }
            />
            <Route
              path="/risk-assessment"
              element={
                <PrivateRoute>
                  <RiskAssessment />
                </PrivateRoute>
              }
            />
            <Route
              path="/insurance-policies"
              element={
                <PrivateRoute>
                  <InsurancePolicies />
                </PrivateRoute>
              }
            />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
    </QueryClientProvider>
  );
}

export default App; 