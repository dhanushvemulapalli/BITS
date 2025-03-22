import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import useAuth from '../hooks/useAuth';

interface InsurancePolicy {
  id: number;
  policy_number: string;
  policy_type: string;
  coverage_amount: number;
  premium_amount: number;
  start_date: string;
  end_date: string;
  status: string;
  coverage_details: {
    inpatient_care: boolean;
    outpatient_care: boolean;
    prescription_drugs: boolean;
    mental_health: boolean;
    dental_care: boolean;
    vision_care: boolean;
  };
  claims_history: {
    total_claims: number;
    approved_claims: number;
    pending_claims: number;
    rejected_claims: number;
  };
}

export default function InsurancePolicies() {
  const { user } = useAuth();

  const { data: policies } = useQuery<InsurancePolicy[]>({
    queryKey: ['insurancePolicies'],
    queryFn: async () => {
      const response = await axios.get('http://localhost:8000/api/v1/insurance/policies');
      return response.data;
    },
  });

  const getStatusColor = (status: string) => {
    switch (status.toLowerCase()) {
      case 'active':
        return 'bg-green-100 text-green-800';
      case 'pending':
        return 'bg-yellow-100 text-yellow-800';
      case 'expired':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Insurance Policies</h1>

      <div className="grid grid-cols-1 gap-6">
        {policies?.map((policy) => (
          <div key={policy.id} className="card">
            <div className="flex justify-between items-start mb-4">
              <div>
                <h2 className="text-xl font-semibold text-gray-900">{policy.policy_type}</h2>
                <p className="text-sm text-gray-500">Policy Number: {policy.policy_number}</p>
              </div>
              <span className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(policy.status)}`}>
                {policy.status}
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h3 className="text-lg font-medium text-gray-900 mb-2">Coverage Details</h3>
                <div className="space-y-2">
                  <p className="flex justify-between">
                    <span className="text-gray-600">Coverage Amount:</span>
                    <span className="font-medium">${policy.coverage_amount.toLocaleString()}</span>
                  </p>
                  <p className="flex justify-between">
                    <span className="text-gray-600">Premium Amount:</span>
                    <span className="font-medium">${policy.premium_amount.toLocaleString()}</span>
                  </p>
                  <p className="flex justify-between">
                    <span className="text-gray-600">Start Date:</span>
                    <span className="font-medium">{new Date(policy.start_date).toLocaleDateString()}</span>
                  </p>
                  <p className="flex justify-between">
                    <span className="text-gray-600">End Date:</span>
                    <span className="font-medium">{new Date(policy.end_date).toLocaleDateString()}</span>
                  </p>
                </div>
              </div>

              <div>
                <h3 className="text-lg font-medium text-gray-900 mb-2">Coverage Benefits</h3>
                <div className="space-y-2">
                  {Object.entries(policy.coverage_details).map(([key, value]) => (
                    <div key={key} className="flex items-center">
                      <span className={`w-2 h-2 rounded-full mr-2 ${value ? 'bg-green-500' : 'bg-red-500'}`}></span>
                      <span className="text-gray-600">
                        {key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            <div className="mt-6">
              <h3 className="text-lg font-medium text-gray-900 mb-2">Claims History</h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div className="bg-gray-50 p-4 rounded-lg">
                  <p className="text-sm text-gray-600">Total Claims</p>
                  <p className="text-xl font-semibold">{policy.claims_history.total_claims}</p>
                </div>
                <div className="bg-green-50 p-4 rounded-lg">
                  <p className="text-sm text-green-600">Approved</p>
                  <p className="text-xl font-semibold text-green-700">{policy.claims_history.approved_claims}</p>
                </div>
                <div className="bg-yellow-50 p-4 rounded-lg">
                  <p className="text-sm text-yellow-600">Pending</p>
                  <p className="text-xl font-semibold text-yellow-700">{policy.claims_history.pending_claims}</p>
                </div>
                <div className="bg-red-50 p-4 rounded-lg">
                  <p className="text-sm text-red-600">Rejected</p>
                  <p className="text-xl font-semibold text-red-700">{policy.claims_history.rejected_claims}</p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
} 