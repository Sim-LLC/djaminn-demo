export default function TextInputComponent({ controlledValue, onChange, onEnter }) {
  return (
    <input
      type="text"
      placeholder="Search..."
      value={controlledValue}
      onChange={onChange}
      onKeyDownCapture={(e) => {
        if (e.key === "Enter") {
          onEnter(e);
        }
      }}
      className="input-search"
    />
  );
}
