# 🛡️ ProtectAPI

ProtectAPI est une API simple et extensible pour gérer :
- les utilisateurs
- les permissions
- les punitions (bans, kicks, etc.)

Conçue pour être rapide à configurer, intuitive à maintenir, et idéale pour les intégrations avec des bots Discord, des jeux ou des outils d'administration.

---

## 🚀 Installation rapide

1. **Clone le repo :**

   ```bash
   git clone https://github.com/tonpseudo/ProtectAPI.git
   cd ProtectAPI
   ```

2. **Lance le script d'installation :**

   ```bash
   python run.py
   ```

   Ce script :
   - crée le dossier `data/` s'il n'existe pas
   - crée le fichier `users.json`
   - te demande ton nom d'utilisateur
   - te donne automatiquement le rôle `admin` si tu es le premier utilisateur

3. **Génère une clé API:**

   ```bash
   python create_api.py
   ```
---

## 🔐 Permissions

- **`admin`** : accès complet à toutes les routes de l'API
- **`moderator`** : peut gérer les punitions et consulter les utilisateurs
- **`user`** : accès en lecture seule à ses propres données
- **`guest`** : accès très limité (consultation publique uniquement)

### Matrice de permissions

| Action | Admin | Moderator | User | Guest |
|--------|-------|-----------|------|-------|
| Créer utilisateur | ✅ | ❌ | ❌ | ❌ |
| Modifier utilisateur | ✅ | ✅ (limité) | ✅ (soi-même) | ❌ |
| Supprimer utilisateur | ✅ | ❌ | ❌ | ❌ |
| Voir tous les utilisateurs | ✅ | ✅ | ❌ | ❌ |
| Bannir/Kick | ✅ | ✅ | ❌ | ❌ |
| Voir historique punitions | ✅ | ✅ | ✅ (soi-même) | ❌ |

---

## 🌐 Routes API

### 🔑 Authentification

- `POST /auth/login` - Connexion utilisateur
- `POST /auth/logout` - Déconnexion
- `POST /auth/register` - Inscription (si activée)
- `GET /auth/me` - Informations du compte connecté

### 👤 Utilisateurs

- `GET /users` - Liste des utilisateurs (admin/moderator)
- `GET /users/{user_id}` - Détails d'un utilisateur
- `POST /users` - Créer un utilisateur (admin)
- `PUT /users/{user_id}` - Modifier un utilisateur
- `DELETE /users/{user_id}` - Supprimer un utilisateur (admin)

### ⚖️ Punitions

- `GET /punishments` - Historique des punitions
- `GET /punishments/{user_id}` - Punitions d'un utilisateur
- `POST /punishments/ban` - Bannir un utilisateur
- `POST /punishments/kick` - Expulser un utilisateur
- `POST /punishments/warn` - Avertir un utilisateur
- `DELETE /punishments/{punishment_id}` - Annuler une punition

### 📊 Statistiques

- `GET /stats/users` - Statistiques utilisateurs
- `GET /stats/punishments` - Statistiques punitions
- `GET /stats/activity` - Activité récente

---

## ⚙️ Configuration

Modifie le fichier `config.py` pour personnaliser ton installation :

```python
# Configuration API
API_HOST = "127.0.0.1"
API_PORT = 8080
DEBUG_MODE = False

# Sécurité
SECRET_KEY = "your-secret-key-here"
TOKEN_EXPIRY = 3600  # 1 heure

# Base de données
DATA_DIR = "./data"
BACKUP_ENABLED = True
BACKUP_INTERVAL = 24  # heures

# Permissions par défaut
DEFAULT_ROLE = "user"
ALLOW_REGISTRATION = False

# Intégrations
DISCORD_WEBHOOK = None
LOG_LEVEL = "INFO"
```

---

## 🔧 Utilisation

### Démarrer l'API

```bash
python api/main.py
```

L'API sera accessible sur `http://localhost:8080`

### Exemple d'utilisation avec curl

```bash
# Connexion
curl -X POST http://localhost:8080/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "motdepasse"}'

# Bannir un utilisateur
curl -X POST http://localhost:8080/punishments/ban \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "123", "reason": "Spam", "duration": 7200}'
```
---

## 🤝 Contribution

Les contributions sont les bienvenues ! Merci de :

1. Fork le projet
2. Créer une branche pour ta feature (`git checkout -b feature/amazing-feature`)
3. Commit tes changements (`git commit -m 'Add amazing feature'`)
4. Push sur la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

### Guidelines

- Code en anglais (variables, fonctions, commentaires)
- Documentation en français pour les utilisateurs
- Tests unitaires pour les nouvelles features
- Respect du style de code existant

---

## 📄 Licence

Ce projet est sous licence GNU. Voir le fichier `LICENSE` pour plus de détails.

---

*ProtectAPI - Simple, rapide, efficace. 🛡️*
