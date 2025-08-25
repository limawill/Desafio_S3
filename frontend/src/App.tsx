import React, { useState } from 'react';
import { isPositiveInteger, isPositiveFloat, isValidDate } from './utils/validators';

function App() {
  // States for input values
  const [text, setText] = useState<string>(''); // For string and sequence
  const [boardSize, setBoardSize] = useState<string>(''); // For board_game
  const [board, setBoard] = useState<string>(''); // For board_game
  const [salary, setSalary] = useState<string>(''); // For benefits
  const [hireDate, setHireDate] = useState<string>(''); // For benefits
  const [resignationDate, setResignationDate] = useState<string>(''); // For benefits
  // State for result
  const [result, setResult] = useState<string | null>(null);
  // State for selected challenge
  const [selectedChallenge, setSelectedChallenge] = useState<string>('string');

  // String validator
  const checkString = async () => {
    try {
      const response = await fetch('/api/v1/string/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setResult(data.is_valid ? 'Valid' : 'Invalid');
    } catch (error) {
      setResult('Error validating');
    }
  };

  // Sequence validator
  const checkSequence = async () => {
    if (!isPositiveInteger(text)) {
      setResult('Please enter only positive integers!');
      return;
    }
    try {
      setResult('Waiting for backend validation...');
      const response = await fetch('/api/v1/sequence/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ position: Number(text) }),
      });
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      setResult('Error validating sequence');
    }
  };

  // Board game validator
  const checkBoardGame = async () => {
    if (!isPositiveInteger(boardSize)) {
      setResult('Board size must be a positive integer!');
      return;
    }
    if (!board) {
      setResult('Please enter the board values!');
      return;
    }
    const boardArray = board.split(',').map(item => {
      const num = Number(item.trim());
      return isNaN(num) ? null : num;
    });
    if (boardArray.includes(null)) {
      setResult('Board values must be numbers only!');
      return;
    }
    if (boardArray.length < Number(boardSize)) {
      setResult('The number of values must be equal to or greater than the board size!');
      return;
    }
    try {
      setResult('Waiting for backend validation...');
      const response = await fetch('/api/v1/board_game/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ board_size: Number(boardSize), board: boardArray }),
      });
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      setResult('Error validating board');
    }
  };

  // Benefits validator
  const checkBenefits = async () => {
    if (!isPositiveFloat(salary)) {
      setResult('Salary must be a positive number!');
      return;
    }
    if (!isValidDate(hireDate)) {
      setResult('Hire date must be in the format YYYY-MM-DD!');
      return;
    }
    if (!isValidDate(resignationDate)) {
      setResult('Resignation date must be in the format YYYY-MM-DD!');
      return;
    }
    try {
      setResult('Waiting for backend validation...');
      const response = await fetch('/api/v1/benefits/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ salary: Number(salary), hire_date: hireDate, resignation_date: resignationDate }),
      });
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      setResult('Error calculating benefits');
    }
  };

  // Handle challenge button click
  const handleChallengeClick = (challenge: string) => {
    setSelectedChallenge(challenge);
    setText('');
    setBoardSize('');
    setBoard('');
    setSalary('');
    setHireDate('');
    setResignationDate('');
    setResult(null);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1 style={{ textAlign: 'center', color: '#333' }}>S3 Challenge</h1>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
        <div style={{ width: '30%', border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
          <button
            onClick={() => handleChallengeClick('string')}
            style={{ display: 'block', width: '100%', padding: '10px', marginBottom: '10px', backgroundColor: selectedChallenge === 'string' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'string' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Challenge 1
          </button>
          <button
            onClick={() => handleChallengeClick('sequence')}
            style={{ display: 'block', width: '100%', padding: '10px', marginBottom: '10px', backgroundColor: selectedChallenge === 'sequence' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'sequence' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Challenge 2
          </button>
          <button
            onClick={() => handleChallengeClick('board_game')}
            style={{ display: 'block', width: '100%', padding: '10px', marginBottom: '10px', backgroundColor: selectedChallenge === 'board_game' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'board_game' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Challenge 3
          </button>
          <button
            onClick={() => handleChallengeClick('benefits')}
            style={{ display: 'block', width: '100%', padding: '10px', backgroundColor: selectedChallenge === 'benefits' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'benefits' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Challenge 4
          </button>
        </div>
        <div style={{ width: '65%', border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
          {selectedChallenge === 'string' && (
            <div>
              <h2 style={{ textAlign: 'center' }}>String Validator</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <input
                  type="text"
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  placeholder="Enter a string (e.g.: BA)"
                  style={{ padding: '10px', margin: '10px 0', width: '70%' }}
                />
                <button
                  onClick={checkString}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', width: 'fit-content' }}
                >
                  Validate
                </button>
              </div>
              {result && (
                <p style={{ marginTop: '10px', fontWeight: 'bold' }}>Result: {result}</p>
              )}
            </div>
          )}
          {selectedChallenge === 'sequence' && (
            <div>
              <h2 style={{ textAlign: 'center' }}>Sequence Validator</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <input
                  type="text"
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  placeholder="Enter a position (e.g.: 5)"
                  style={{ padding: '10px', margin: '10px 0', width: '70%' }}
                />
                <button
                  onClick={checkSequence}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', width: 'fit-content' }}
                >
                  Validate Sequence
                </button>
              </div>
              {result && (
                <pre style={{ marginTop: '10px', fontWeight: 'bold', whiteSpace: 'pre-wrap' }}>Result: {result}</pre>
              )}
            </div>
          )}
          {selectedChallenge === 'board_game' && (
            <div>
              <h2 style={{ textAlign: 'center' }}>Board Validator</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <input
                  type="text"
                  value={boardSize}
                  onChange={(e) => setBoardSize(e.target.value)}
                  placeholder="Board size (e.g.: 5)"
                  style={{ padding: '10px', margin: '10px 0', width: '30%' }}
                />
                <input
                  type="text"
                  value={board}
                  onChange={(e) => setBoard(e.target.value)}
                  placeholder="Board values (e.g.: 0,1,1,2,3)"
                  style={{ padding: '10px', margin: '10px 0', width: '70%' }}
                />
                <button
                  onClick={checkBoardGame}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', width: 'fit-content' }}
                >
                  Validate Board
                </button>
              </div>
              {result && (
                <pre style={{ marginTop: '10px', fontWeight: 'bold', whiteSpace: 'pre-wrap' }}>Result: {result}</pre>
              )}
            </div>
          )}
          {selectedChallenge === 'benefits' && (
            <div>
              <h2 style={{ textAlign: 'left' }}>Benefits Calculation</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '400px' }}>
                <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'center' }}>
                  <label style={{ fontWeight: 'bold', width: '120px', textAlign: 'left', marginRight: '10px' }}>Salary:</label>
                  <input
                    type="number"
                    value={salary}
                    onChange={(e) => setSalary(e.target.value)}
                    placeholder="Salary (e.g.: 1000)"
                    style={{ padding: '10px', width: '200px', flex: '1' }}
                    step="0.01"
                  />
                </div>
                <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'center' }}>
                  <label style={{ fontWeight: 'bold', width: '120px', textAlign: 'left', marginRight: '10px' }}>Hire Date:</label>
                  <input
                    type="text"
                    value={hireDate}
                    onChange={(e) => {
                      const value = e.target.value.replace(/[^0-9-]/g, '');
                      if (value.length <= 10) setHireDate(value);
                    }}
                    placeholder="Hire date (YYYY-MM-DD)"
                    style={{ padding: '10px', width: '200px', flex: '1' }}
                    maxLength={10}
                  />
                </div>
                <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'center' }}>
                  <label style={{ fontWeight: 'bold', width: '120px', textAlign: 'left', marginRight: '10px' }}>Resignation Date:</label>
                  <input
                    type="text"
                    value={resignationDate}
                    onChange={(e) => {
                      const value = e.target.value.replace(/[^0-9-]/g, '');
                      if (value.length <= 10) setResignationDate(value);
                    }}
                    placeholder="Resignation date (YYYY-MM-DD)"
                    style={{ padding: '10px', width: '200px', flex: '1' }}
                    maxLength={10}
                  />
                </div>
                <button
                  onClick={checkBenefits}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', alignSelf: 'flex-start', marginTop: '10px' }}
                >
                  Calculate Benefits
                </button>
              </div>
              {result && (
                <pre style={{ marginTop: '10px', fontWeight: 'bold', whiteSpace: 'pre-wrap', textAlign: 'left' }}>Result: {result}</pre>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;