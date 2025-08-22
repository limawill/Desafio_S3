import React, { useState } from 'react';
import { isPositiveInteger, isPositiveFloat, isValidDate } from './utils/validators';

function App() {
  // Estados para os valores digitados
  const [text, setText] = useState<string>(''); // Para string e sequence
  const [boardSize, setBoardSize] = useState<string>(''); // Para board_game
  const [board, setBoard] = useState<string>(''); // Para board_game
  const [salary, setSalary] = useState<string>(''); // Para benefits
  const [hireDate, setHireDate] = useState<string>(''); // Para benefits
  const [resignationDate, setResignationDate] = useState<string>(''); // Para benefits
  // Estado para o resultado
  const [result, setResult] = useState<string | null>(null);
  // Estado para o desafio selecionado
  const [selectedChallenge, setSelectedChallenge] = useState<string>('string');

  // Função para validar string
  const checkString = async () => {
    try {
      const response = await fetch('/api/v1/string/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setResult(data.is_valid ? 'Válido' : 'Inválido');
    } catch (error) {
      setResult('Erro ao validar');
    }
  };

  // Função para validar sequência
  const checkSequence = async () => {
    if (!isPositiveInteger(text)) {
      setResult('Digite apenas números inteiros positivos!');
      return;
    }
    try {
      setResult('Aguardando validação do backend...');
      const response = await fetch('/api/v1/sequence/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ position: Number(text) }),
      });
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      setResult('Erro ao validar sequência');
    }
  };

  // Função para validar board game
  const checkBoardGame = async () => {
    if (!isPositiveInteger(boardSize)) {
      setResult('O tamanho do tabuleiro deve ser um número inteiro positivo!');
      return;
    }
    if (!board) {
      setResult('Por favor, digite os valores do tabuleiro!');
      return;
    }
    const boardArray = board.split(',').map(item => {
      const num = Number(item.trim());
      return isNaN(num) ? null : num;
    });
    if (boardArray.includes(null)) {
      setResult('Os valores do tabuleiro devem ser apenas números!');
      return;
    }
    if (boardArray.length < Number(boardSize)) {
      setResult('O número de valores precisa ser igual ou maior que o tamanho do tabuleiro!');
      return;
    }
    try {
      setResult('Aguardando validação do backend...');
      const response = await fetch('/api/v1/board_game/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ board_size: Number(boardSize), board: boardArray }),
      });
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      setResult('Erro ao validar tabuleiro');
    }
  };

  // Função para validar benefits
  const checkBenefits = async () => {
    if (!isPositiveFloat(salary)) {
      setResult('O salário deve ser um número positivo!');
      return;
    }
    if (!isValidDate(hireDate)) {
      setResult('Data de contratação deve estar no formato YYYY-MM-DD!');
      return;
    }
    if (!isValidDate(resignationDate)) {
      setResult('Data de demissão deve estar no formato YYYY-MM-DD!');
      return;
    }
    try {
      setResult('Aguardando validação do backend...');
      const response = await fetch('/api/v1/benefits/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ salary: Number(salary), hire_date: hireDate, resignation_date: resignationDate }),
      });
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      setResult('Erro ao calcular benefícios');
    }
  };

  // Função para lidar com o clique nos botões
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
      <h1 style={{ textAlign: 'center', color: '#333' }}>Desafio S3</h1>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
        <div style={{ width: '30%', border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
          <button
            onClick={() => handleChallengeClick('string')}
            style={{ display: 'block', width: '100%', padding: '10px', marginBottom: '10px', backgroundColor: selectedChallenge === 'string' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'string' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Desafio 1
          </button>
          <button
            onClick={() => handleChallengeClick('sequence')}
            style={{ display: 'block', width: '100%', padding: '10px', marginBottom: '10px', backgroundColor: selectedChallenge === 'sequence' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'sequence' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Desafio 2
          </button>
          <button
            onClick={() => handleChallengeClick('board_game')}
            style={{ display: 'block', width: '100%', padding: '10px', marginBottom: '10px', backgroundColor: selectedChallenge === 'board_game' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'board_game' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Desafio 3
          </button>
          <button
            onClick={() => handleChallengeClick('benefits')}
            style={{ display: 'block', width: '100%', padding: '10px', backgroundColor: selectedChallenge === 'benefits' ? '#2196F3' : '#f0f0f0', color: selectedChallenge === 'benefits' ? 'white' : 'black', border: 'none', cursor: 'pointer' }}
          >
            Desafio 4
          </button>
        </div>
        <div style={{ width: '65%', border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
          {selectedChallenge === 'string' && (
            <div>
              <h2 style={{ textAlign: 'center' }}>Validador de String</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <input
                  type="text"
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  placeholder="Digite uma string (ex.: BA)"
                  style={{ padding: '10px', margin: '10px 0', width: '70%' }}
                />
                <button
                  onClick={checkString}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', width: 'fit-content' }}
                >
                  Validar
                </button>
              </div>
              {result && (
                <p style={{ marginTop: '10px', fontWeight: 'bold' }}>Return: {result}</p>
              )}
            </div>
          )}
          {selectedChallenge === 'sequence' && (
            <div>
              <h2 style={{ textAlign: 'center' }}>Validador de Sequência</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <input
                  type="text"
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  placeholder="Digite uma posição (ex.: 5)"
                  style={{ padding: '10px', margin: '10px 0', width: '70%' }}
                />
                <button
                  onClick={checkSequence}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', width: 'fit-content' }}
                >
                  Validar Sequência
                </button>
              </div>
              {result && (
                <pre style={{ marginTop: '10px', fontWeight: 'bold', whiteSpace: 'pre-wrap' }}>Return: {result}</pre>
              )}
            </div>
          )}
          {selectedChallenge === 'board_game' && (
            <div>
              <h2 style={{ textAlign: 'center' }}>Validador de Tabuleiro</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <input
                  type="text"
                  value={boardSize}
                  onChange={(e) => setBoardSize(e.target.value)}
                  placeholder="Tamanho do tabuleiro (ex.: 5)"
                  style={{ padding: '10px', margin: '10px 0', width: '30%' }}
                />
                <input
                  type="text"
                  value={board}
                  onChange={(e) => setBoard(e.target.value)}
                  placeholder="Valores do tabuleiro (ex.: 0,1,1,2,3)"
                  style={{ padding: '10px', margin: '10px 0', width: '70%' }}
                />
                <button
                  onClick={checkBoardGame}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', width: 'fit-content' }}
                >
                  Validar Tabuleiro
                </button>
              </div>
              {result && (
                <pre style={{ marginTop: '10px', fontWeight: 'bold', whiteSpace: 'pre-wrap' }}>Return: {result}</pre>
              )}
            </div>
          )}
          {selectedChallenge === 'benefits' && (
            <div>
              <h2 style={{ textAlign: 'left' }}>Cálculo de Benefícios</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '400px' }}>
                <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'center' }}>
                  <label style={{ fontWeight: 'bold', width: '120px', textAlign: 'left', marginRight: '10px' }}>Salary:</label>
                  <input
                    type="number"
                    value={salary}
                    onChange={(e) => setSalary(e.target.value)}
                    placeholder="Salário (ex.: 1000)"
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
                    placeholder="Data de Contratação (YYYY-MM-DD)"
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
                    placeholder="Data de Demissão (YYYY-MM-DD)"
                    style={{ padding: '10px', width: '200px', flex: '1' }}
                    maxLength={10}
                  />
                </div>
                <button
                  onClick={checkBenefits}
                  style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer', alignSelf: 'flex-start', marginTop: '10px' }}
                >
                  Calcular Benefícios
                </button>
              </div>
              {result && (
                <pre style={{ marginTop: '10px', fontWeight: 'bold', whiteSpace: 'pre-wrap', textAlign: 'left' }}>Return: {result}</pre>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;