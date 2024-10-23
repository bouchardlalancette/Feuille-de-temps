// Fonction pour calculer le total des heures
function calculateTotalHours() {
    // Sélectionner tous les champs de saisie de type "number"
    document.querySelectorAll('input[type="number"]').forEach(input => {
        // Ajouter un écouteur d'événements pour recalculer le total chaque fois qu'une valeur est changée
        input.addEventListener('input', () => {
            let total = 0;  // Initialiser le total à zéro
            // Parcourir tous les champs de saisie pour cumuler les heures
            document.querySelectorAll('input[type="number"]').forEach(dayInput => {
                if (dayInput.id !== 'total_hours') {  // Ignorer le champ du total
                    total += parseFloat(dayInput.value) || 0;  // Ajouter la valeur de chaque champ au total
                }
            });
            // Mettre à jour le champ du total avec la somme calculée, arrondie à deux décimales
            document.getElementById('total_hours').value = total.toFixed(2);
        });
    });
}

// Appeler la fonction lors du chargement de la page
window.onload = calculateTotalHours;
