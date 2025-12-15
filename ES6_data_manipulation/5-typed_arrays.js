export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer); // using setInt8 here does not return detailed view
  view.setInt8(position, value); // moved setting on its own line, separated from DataView creation
  return view;
}
