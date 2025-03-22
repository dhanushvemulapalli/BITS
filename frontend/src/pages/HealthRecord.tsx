import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import useAuth from '../hooks/useAuth';

interface HealthRecord {
  id: number;
  patient_id: number;
  height: number;
  weight: number;
  bmi: number;
  blood_pressure: {
    systolic: number;
    diastolic: number;
    unit: string;
  };
  heart_rate: number;
  cholesterol: {
    total: number;
    hdl: number;
    ldl: number;
    triglycerides: number;
    unit: string;
  };
  blood_sugar: {
    fasting: number;
    post_meal: number;
    unit: string;
  };
  medical_conditions: string[];
  medications: {
    name: string;
    dosage: string;
    frequency: string;
    start_date: string;
    end_date?: string;
  }[];
  allergies: string[];
  immunizations: {
    name: string;
    date: string;
    provider: string;
    next_due_date?: string;
  }[];
  last_updated: string;
}

export default function HealthRecord() {
  const { user } = useAuth();

  const { data: healthRecord } = useQuery<HealthRecord>({
    queryKey: ['healthRecord'],
    queryFn: async () => {
      const response = await axios.get('http://localhost:8000/api/v1/health-record');
      return response.data;
    },
  });

  const getBMICategory = (bmi: number) => {
    if (bmi < 18.5) return 'Underweight';
    if (bmi < 25) return 'Normal';
    if (bmi < 30) return 'Overweight';
    return 'Obese';
  };

  const getBMIColor = (bmi: number) => {
    if (bmi < 18.5) return 'text-yellow-600';
    if (bmi < 25) return 'text-green-600';
    if (bmi < 30) return 'text-orange-600';
    return 'text-red-600';
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Health Record</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Basic Information</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Height & Weight</h3>
              <div className="grid grid-cols-2 gap-4 mt-2">
                <div>
                  <p className="text-sm text-gray-500">Height</p>
                  <p className="text-lg font-medium">{healthRecord?.height} cm</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Weight</p>
                  <p className="text-lg font-medium">{healthRecord?.weight} kg</p>
                </div>
              </div>
              <div className="mt-2">
                <p className="text-sm text-gray-500">BMI</p>
                <p className={`text-lg font-medium ${getBMIColor(healthRecord?.bmi || 0)}`}>
                  {healthRecord?.bmi?.toFixed(1)} ({getBMICategory(healthRecord?.bmi || 0)})
                </p>
              </div>
            </div>

            <div>
              <h3 className="text-lg font-medium text-gray-900">Blood Pressure</h3>
              <p className="text-lg font-medium mt-2">
                {healthRecord?.blood_pressure.systolic}/{healthRecord?.blood_pressure.diastolic} {healthRecord?.blood_pressure.unit}
              </p>
            </div>

            <div>
              <h3 className="text-lg font-medium text-gray-900">Heart Rate</h3>
              <p className="text-lg font-medium mt-2">{healthRecord?.heart_rate} bpm</p>
            </div>
          </div>
        </div>

        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Blood Work</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Cholesterol</h3>
              <div className="space-y-2 mt-2">
                <p className="flex justify-between">
                  <span className="text-gray-600">Total:</span>
                  <span className="font-medium">{healthRecord?.cholesterol.total} {healthRecord?.cholesterol.unit}</span>
                </p>
                <p className="flex justify-between">
                  <span className="text-gray-600">HDL:</span>
                  <span className="font-medium">{healthRecord?.cholesterol.hdl} {healthRecord?.cholesterol.unit}</span>
                </p>
                <p className="flex justify-between">
                  <span className="text-gray-600">LDL:</span>
                  <span className="font-medium">{healthRecord?.cholesterol.ldl} {healthRecord?.cholesterol.unit}</span>
                </p>
                <p className="flex justify-between">
                  <span className="text-gray-600">Triglycerides:</span>
                  <span className="font-medium">{healthRecord?.cholesterol.triglycerides} {healthRecord?.cholesterol.unit}</span>
                </p>
              </div>
            </div>

            <div>
              <h3 className="text-lg font-medium text-gray-900">Blood Sugar</h3>
              <div className="space-y-2 mt-2">
                <p className="flex justify-between">
                  <span className="text-gray-600">Fasting:</span>
                  <span className="font-medium">{healthRecord?.blood_sugar.fasting} {healthRecord?.blood_sugar.unit}</span>
                </p>
                <p className="flex justify-between">
                  <span className="text-gray-600">Post Meal:</span>
                  <span className="font-medium">{healthRecord?.blood_sugar.post_meal} {healthRecord?.blood_sugar.unit}</span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Medical Conditions</h2>
          <ul className="space-y-2">
            {healthRecord?.medical_conditions?.map((condition, index) => (
              <li key={index} className="flex items-start">
                <span className="w-2 h-2 bg-red-500 rounded-full mr-2 mt-2"></span>
                {condition}
              </li>
            ))}
          </ul>
        </div>

        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Allergies</h2>
          <ul className="space-y-2">
            {healthRecord?.allergies?.map((allergy, index) => (
              <li key={index} className="flex items-start">
                <span className="w-2 h-2 bg-yellow-500 rounded-full mr-2 mt-2"></span>
                {allergy}
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="card">
        <h2 className="text-xl font-semibold mb-4">Current Medications</h2>
        <div className="space-y-4">
          {healthRecord?.medications?.map((medication, index) => (
            <div key={index} className="border-b border-gray-200 pb-4 last:border-0">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-medium text-gray-900">{medication.name}</h3>
                  <p className="text-sm text-gray-500">{medication.dosage} - {medication.frequency}</p>
                </div>
                <div className="text-sm text-gray-500">
                  Started: {new Date(medication.start_date).toLocaleDateString()}
                  {medication.end_date && ` - End: ${new Date(medication.end_date).toLocaleDateString()}`}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="card">
        <h2 className="text-xl font-semibold mb-4">Immunizations</h2>
        <div className="space-y-4">
          {healthRecord?.immunizations?.map((immunization, index) => (
            <div key={index} className="border-b border-gray-200 pb-4 last:border-0">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-medium text-gray-900">{immunization.name}</h3>
                  <p className="text-sm text-gray-500">Provider: {immunization.provider}</p>
                </div>
                <div className="text-sm text-gray-500">
                  Date: {new Date(immunization.date).toLocaleDateString()}
                  {immunization.next_due_date && ` - Next Due: ${new Date(immunization.next_due_date).toLocaleDateString()}`}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="text-sm text-gray-500">
        Last Updated: {healthRecord ? new Date(healthRecord.last_updated).toLocaleDateString() : 'N/A'}
      </div>
    </div>
  );
} 