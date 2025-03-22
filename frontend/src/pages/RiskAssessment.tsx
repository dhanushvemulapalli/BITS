import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import useAuth from '../hooks/useAuth';

interface RiskAssessment {
  id: number;
  overall_risk_score: number;
  risk_level: string;
  cardiovascular_risk: number;
  respiratory_risk: number;
  metabolic_risk: number;
  lifestyle_risk: number;
  predicted_health_issues: string[];
  risk_factors: string[];
  recommendations: string[];
  model_version: string;
  prediction_confidence: number;
}

export default function RiskAssessment() {
  const { user } = useAuth();

  const { data: riskAssessment } = useQuery<RiskAssessment>({
    queryKey: ['riskAssessment'],
    queryFn: async () => {
      const response = await axios.get('http://localhost:8000/api/v1/risk-assessment/latest');
      return response.data;
    },
  });

  const getRiskLevelColor = (riskLevel: string | undefined) => {
    if (!riskLevel) return 'text-gray-600';
    
    switch (riskLevel.toLowerCase()) {
      case 'low':
        return 'text-green-600';
      case 'moderate':
        return 'text-yellow-600';
      case 'high':
        return 'text-red-600';
      default:
        return 'text-gray-600';
    }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Risk Assessment</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Overall Risk Assessment</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Risk Score</h3>
              <p className={`text-3xl font-bold ${getRiskLevelColor(riskAssessment?.risk_level)}`}>
                {riskAssessment?.overall_risk_score || 'N/A'}
              </p>
              <p className="text-sm text-gray-500">Risk Level: {riskAssessment?.risk_level || 'N/A'}</p>
            </div>
            <div>
              <h3 className="text-lg font-medium text-gray-900">Prediction Confidence</h3>
              <p className="text-2xl font-bold text-indigo-600">
                {(riskAssessment?.prediction_confidence || 0) * 100}%
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Component Risk Scores</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Cardiovascular Risk</h3>
              <div className="w-full bg-gray-200 rounded-full h-2.5">
                <div
                  className="bg-red-600 h-2.5 rounded-full"
                  style={{ width: `${riskAssessment?.cardiovascular_risk || 0}%` }}
                ></div>
              </div>
              <p className="text-sm text-gray-500">{riskAssessment?.cardiovascular_risk || 0}%</p>
            </div>
            <div>
              <h3 className="text-lg font-medium text-gray-900">Respiratory Risk</h3>
              <div className="w-full bg-gray-200 rounded-full h-2.5">
                <div
                  className="bg-yellow-600 h-2.5 rounded-full"
                  style={{ width: `${riskAssessment?.respiratory_risk || 0}%` }}
                ></div>
              </div>
              <p className="text-sm text-gray-500">{riskAssessment?.respiratory_risk || 0}%</p>
            </div>
            <div>
              <h3 className="text-lg font-medium text-gray-900">Metabolic Risk</h3>
              <div className="w-full bg-gray-200 rounded-full h-2.5">
                <div
                  className="bg-green-600 h-2.5 rounded-full"
                  style={{ width: `${riskAssessment?.metabolic_risk || 0}%` }}
                ></div>
              </div>
              <p className="text-sm text-gray-500">{riskAssessment?.metabolic_risk || 0}%</p>
            </div>
            <div>
              <h3 className="text-lg font-medium text-gray-900">Lifestyle Risk</h3>
              <div className="w-full bg-gray-200 rounded-full h-2.5">
                <div
                  className="bg-blue-600 h-2.5 rounded-full"
                  style={{ width: `${riskAssessment?.lifestyle_risk || 0}%` }}
                ></div>
              </div>
              <p className="text-sm text-gray-500">{riskAssessment?.lifestyle_risk || 0}%</p>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Predicted Health Issues</h2>
          <ul className="space-y-2">
            {riskAssessment?.predicted_health_issues?.map((issue, index) => (
              <li key={index} className="flex items-start">
                <span className="w-2 h-2 bg-red-500 rounded-full mr-2 mt-2"></span>
                {issue}
              </li>
            ))}
          </ul>
        </div>

        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Risk Factors</h2>
          <ul className="space-y-2">
            {riskAssessment?.risk_factors?.map((factor, index) => (
              <li key={index} className="flex items-start">
                <span className="w-2 h-2 bg-yellow-500 rounded-full mr-2 mt-2"></span>
                {factor}
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="card">
        <h2 className="text-xl font-semibold mb-4">Recommendations</h2>
        <ul className="space-y-2">
          {riskAssessment?.recommendations?.map((recommendation, index) => (
            <li key={index} className="flex items-start">
              <span className="w-2 h-2 bg-green-500 rounded-full mr-2 mt-2"></span>
              {recommendation}
            </li>
          ))}
        </ul>
      </div>

      <div className="text-sm text-gray-500">
        <p>Model Version: {riskAssessment?.model_version || 'N/A'}</p>
        <p>Last Updated: {riskAssessment ? new Date().toLocaleDateString() : 'N/A'}</p>
      </div>
    </div>
  );
} 