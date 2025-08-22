export function isPositiveInteger(value: string): boolean {
  const num = Number(value);
  return Number.isInteger(num) && num > 0;
}

export function isPositiveFloat(value: string): boolean {
  const num = Number(value);
  return !isNaN(num) && num > 0;
}

export function isValidDate(value: string): boolean {
  return /^\d{4}-\d{2}-\d{2}$/.test(value);
}
