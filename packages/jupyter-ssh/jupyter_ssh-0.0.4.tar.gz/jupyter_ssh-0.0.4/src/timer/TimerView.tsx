import { useEffect } from 'react';
import useStore from '../state';

export const TimerView = () =>  {
  const { timer, increaseTimer, secondsPassed } = useStore();
  useEffect(() => {
    setInterval(() => {
      increaseTimer();
    }, 1000);
  }, []);
  return (
    <button onClick={() => timer.reset()}>
      Jupyter SSH: {secondsPassed}
    </button>
  )
}
