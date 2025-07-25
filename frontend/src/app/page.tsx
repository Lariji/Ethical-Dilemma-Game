'use client';

import { useState } from 'react';

export default function HomePage() {
  const [dilemma, setDilemma] = useState('');
  const [frameworks, setFrameworks] = useState<string[]>(['deontology', 'utilitarianism', 'virtue']);

  const handleToggle = (fw: string) => {
    setFrameworks(prev =>
      prev.includes(fw) ? prev.filter(f => f !== fw) : [...prev, fw]
    );
  };

  const handleSubmit = () => {
    const params = new URLSearchParams({
      dilemma,
      frameworks: frameworks.join(','),
    });
    window.location.href = `/results?${params.toString()}`;
  };

  return (
    <main className="min-h-screen bg-gray-100 p-6 flex flex-col items-center">
      <h1 className="text-3xl bg-black-200 font-bold mb-6">AI Moral Philosopher</h1>

      <textarea
        className="w-full max-w-xl h-40 p-4 rounded-md border border-gray-300 mb-4"
        placeholder="Enter a moral dilemma..."
        value={dilemma}
        onChange={(e) => setDilemma(e.target.value)}
      />

      <div className="mb-4">
        <label className="block font-semibold mb-2">Choose frameworks:</label>
        {['deontology', 'utilitarianism', 'virtue'].map(fw => (
          <label key={fw} className="mr-4">
            <input
              type="checkbox"
              checked={frameworks.includes(fw)}
              onChange={() => handleToggle(fw)}
            />{' '}
            {fw.charAt(0).toUpperCase() + fw.slice(1)}
          </label>
        ))}
      </div>

      <button
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
        onClick={handleSubmit}
        disabled={!dilemma}
      >
        Submit
      </button>
    </main>
  );
}