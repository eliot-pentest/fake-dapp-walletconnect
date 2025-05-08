# Fausse dApp WalletConnect

Ce projet est une **fausse dApp** qui génère un QR code compatible avec Trust Wallet et simule une connexion à un contrat TRON via WalletConnect. Le but est de tester les connexions et observer les signatures sur la blockchain dans le cadre d'un **test de pénétration autorisé**.

## 🚨 Attention
Ce projet doit être utilisé uniquement dans le cadre légal et pour des tests autorisés. Toute utilisation abusive est interdite et pourrait être illégale.

---

## 🚀 Déploiement

Ce projet utilise **Flask** pour créer un serveur backend minimal qui gère les requêtes WalletConnect et génère des QR codes pour simuler la connexion à un contrat intelligent.

### Étapes de déploiement :

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/<ton-utilisateur>/fake-dapp-walletconnect.git
   cd fake-dapp-walletconnect
   ```

2. **Installer les dépendances :**

   Assurez-vous d’avoir Python 3 installé, puis exécutez :

   ```bash
   pip install -r requirements.txt
   ```

3. **Exécuter l'application Flask localement :**

   Lance l'application Flask :

   ```bash
   python app.py
   ```

   Par défaut, le serveur écoute sur `http://127.0.0.1:5000/`.

4. **Déployer sur Render (optionnel) :**

   Si vous voulez héberger cette application gratuitement, suivez ces étapes :
   - Créez un compte sur [Render](https://render.com)
   - Créez un nouveau **Web Service** connecté à ce dépôt GitHub.
   - Dans les paramètres de déploiement, utilisez :
     - **Build Command** : `pip install -r requirements.txt`
     - **Start Command** : `python app.py`

5. **Générer le QR Code :**

   Une fois le projet déployé, exécutez le script `generate_qr.py` pour générer un QR code avec l'URL de votre dApp.

   ```bash
   python generate_qr.py
   ```

   Vous pouvez maintenant scanner ce QR code avec Trust Wallet.

---

## 🧑‍💻 Technologies utilisées :

- **Flask** - Framework Python léger pour le backend
- **TRON** - Blockchain pour la gestion des contrats
- **QR Code** - Génération de QR code pour WalletConnect
- **HTML/CSS** - Interface utilisateur simple et stylisée

---

## 🔐 Avertissement de sécurité

Cette dApp est conçue dans un but purement éducatif et pour des tests de pénétration autorisés. Toute tentative d'exploitation sans autorisation est illégale. Utilisez ce projet uniquement dans des environnements contrôlés et éthiques.

---

## 📜 License

Ce projet est sous la licence **MIT**. Vous pouvez l'utiliser, le modifier et le distribuer librement, à condition de respecter les termes de cette licence.
