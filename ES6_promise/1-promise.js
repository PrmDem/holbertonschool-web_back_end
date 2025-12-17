export default function getFullResponseFromAPI(success) {
  const res = { 'status': 200, 'body': 'Success' };

  if (success === true) {
    return Promise.resolve(res);
  } else {
    return Promise.reject(new Error("The fake API is not working currently"));
  }
}
