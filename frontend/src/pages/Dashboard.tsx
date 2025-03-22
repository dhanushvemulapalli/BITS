import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import useAuth from '../hooks/useAuth';
import axios from 'axios';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

interface HealthMetrics {
  date: string;
  bmi: number;
  blood_pressure_systolic: number;
  blood_pressure_diastolic: number;
  heart_rate: number;
}

interface RiskAssessment {
  overall_risk_score: number;
  risk_level: string;
  cardiovascular_risk: number;
  respiratory_risk: number;
  metabolic_risk: number;
  lifestyle_risk: number;
}

export default function Dashboard() {
  const { user } = useAuth();

  const { data: healthMetrics } = useQuery<HealthMetrics[]>({
    queryKey: ['healthMetrics'],
    queryFn: async () => {
      const response = await axios.get('http://localhost:8000/api/v1/health-records/metrics');
      return response.data;
    },
  });

  const { data: riskAssessment } = useQuery<RiskAssessment>({
    queryKey: ['riskAssessment'],
    queryFn: async () => {
      const response = await axios.get('http://localhost:8000/api/v1/risk-assessment/latest');
      return response.data;
    },
  });

  const chartData = {
    labels: healthMetrics?.map((metric) => metric.date) || [],
    datasets: [
      {
        label: 'BMI',
        data: healthMetrics?.map((metric) => metric.bmi) || [],
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
      {
        label: 'Systolic BP',
        data: healthMetrics?.map((metric) => metric.blood_pressure_systolic) || [],
        borderColor: 'rgb(255, 99, 132)',
        tension: 0.1,
      },
      {
        label: 'Diastolic BP',
        data: healthMetrics?.map((metric) => metric.blood_pressure_diastolic) || [],
        borderColor: 'rgb(53, 162, 235)',
        tension: 0.1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      title: {
        display: true,
        text: 'Health Metrics Over Time',
      },
    },
  };

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Overall Risk Score</h3>
          <p className="mt-2 text-3xl font-bold text-indigo-600">
            {riskAssessment?.overall_risk_score || 'N/A'}
          </p>
          <p className="text-sm text-gray-500">Risk Level: {riskAssessment?.risk_level || 'N/A'}</p>
        </div>
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Cardiovascular Risk</h3>
          <p className="mt-2 text-3xl font-bold text-red-600">
            {riskAssessment?.cardiovascular_risk || 'N/A'}%
          </p>
        </div>
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Latest BMI</h3>
          <p className="mt-2 text-3xl font-bold text-green-600">
            {healthMetrics?.[healthMetrics.length - 1]?.bmi || 'N/A'}
          </p>
        </div>
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Latest BP</h3>
          <p className="mt-2 text-3xl font-bold text-blue-600">
            {healthMetrics?.[healthMetrics.length - 1]?.blood_pressure_systolic || 'N/A'}/
            {healthMetrics?.[healthMetrics.length - 1]?.blood_pressure_diastolic || 'N/A'}
          </p>
        </div>
      </div>

      <div className="card">
        <Line options={chartOptions} data={chartData} />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Risk Factors</h3>
          <ul className="mt-4 space-y-2">
            <li className="flex items-center">
              <span className="w-2 h-2 bg-red-500 rounded-full mr-2"></span>
              Cardiovascular Risk: {riskAssessment?.cardiovascular_risk || 'N/A'}%
            </li>
            <li className="flex items-center">
              <span className="w-2 h-2 bg-yellow-500 rounded-full mr-2"></span>
              Respiratory Risk: {riskAssessment?.respiratory_risk || 'N/A'}%
            </li>
            <li className="flex items-center">
              <span className="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
              Metabolic Risk: {riskAssessment?.metabolic_risk || 'N/A'}%
            </li>
            <li className="flex items-center">
              <span className="w-2 h-2 bg-blue-500 rounded-full mr-2"></span>
              Lifestyle Risk: {riskAssessment?.lifestyle_risk || 'N/A'}%
            </li>
          </ul>
        </div>

        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Recommendations</h3>
          <ul className="mt-4 space-y-2">
            <li className="flex items-start">
              <span className="w-2 h-2 bg-indigo-500 rounded-full mr-2 mt-2"></span>
              Regular exercise and physical activity
            </li>
            <li className="flex items-start">
              <span className="w-2 h-2 bg-indigo-500 rounded-full mr-2 mt-2"></span>
              Balanced diet with reduced salt intake
            </li>
            <li className="flex items-start">
              <span className="w-2 h-2 bg-indigo-500 rounded-full mr-2 mt-2"></span>
              Regular health check-ups
            </li>
            <li className="flex items-start">
              <span className="w-2 h-2 bg-indigo-500 rounded-full mr-2 mt-2"></span>
              Stress management and adequate sleep
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
} 