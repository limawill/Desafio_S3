import { isPositiveInteger, isPositiveFloat, isValidDate } from '../utils/validators';

describe('validators', () => {
  test('isPositiveInteger', () => {
    expect(isPositiveInteger('5')).toBe(true);
    expect(isPositiveInteger('0')).toBe(false);
    expect(isPositiveInteger('-1')).toBe(false);
    expect(isPositiveInteger('abc')).toBe(false);
  });

  test('isPositiveFloat', () => {
    expect(isPositiveFloat('5.5')).toBe(true);
    expect(isPositiveFloat('0')).toBe(false);
    expect(isPositiveFloat('-1.2')).toBe(false);
    expect(isPositiveFloat('abc')).toBe(false);
  });

  test('isValidDate', () => {
    expect(isValidDate('2023-01-01')).toBe(true);
    expect(isValidDate('01-01-2023')).toBe(false);
    expect(isValidDate('2023/01/01')).toBe(false);
    expect(isValidDate('')).toBe(false);
  });
});