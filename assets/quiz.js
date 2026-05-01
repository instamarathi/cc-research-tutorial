document.addEventListener('DOMContentLoaded', () => {
  // MCQ blocks
  document.querySelectorAll('.mcq-block').forEach(block => {
    const options = block.querySelectorAll('.mcq-option');
    const explanation = block.querySelector('.explanation');
    let answered = false;

    options.forEach(btn => {
      btn.addEventListener('click', () => {
        if (answered) return;
        answered = true;

        options.forEach(o => {
          o.disabled = true;
          if (o.dataset.correct === 'true') {
            o.classList.add('correct');
          }
        });

        if (btn.dataset.correct !== 'true') {
          btn.classList.add('wrong');
        }

        if (explanation) {
          explanation.classList.remove('hidden');
        }
      });
    });
  });

  // Thinking exercise reveal
  document.querySelectorAll('.think-block').forEach(block => {
    const btn = block.querySelector('.reveal-btn');
    const answer = block.querySelector('.answer');
    if (!btn || !answer) return;

    btn.addEventListener('click', () => {
      if (answer.classList.contains('hidden')) {
        answer.classList.remove('hidden');
        btn.textContent = 'Hide answer';
      } else {
        answer.classList.add('hidden');
        btn.textContent = 'Reveal suggested answer';
      }
    });
  });
});
