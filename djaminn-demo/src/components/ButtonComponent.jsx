export default function ButtonComponent({ buttonText, onClick }) {
    return (
        <button onClick={onClick} className="btn btn-primary">
            {buttonText}
        </button>
    );
}