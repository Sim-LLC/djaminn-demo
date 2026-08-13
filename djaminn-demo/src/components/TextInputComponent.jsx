export default function TextInputComponent({ controlledValue, onChange }) {
  return (
    <input
      type="text"
      placeholder="Search..."
      value={controlledValue}
      onChange={onChange}
      className="input-search"
    />
  );
}
