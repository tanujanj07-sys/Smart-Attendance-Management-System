function startQR() {
  const status = document.getElementById("status");
  status.textContent = "Starting QR scanner...";

  const scanner = new Html5QrcodeScanner("qr-reader", {
    fps: 10,
    qrbox: { width: 250, height: 250 },
    rememberLastUsedCamera: true,
    aspectRatio: 1.7777778
  });

  scanner.render(
    (decodedText, decodedResult) => {
      status.textContent = "QR Scanned: " + decodedText;
      console.log(decodedText, decodedResult);
      scanner.clear();
    },
    (error) => {
      console.log(error);
    }
  );
}