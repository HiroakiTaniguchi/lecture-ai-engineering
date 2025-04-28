{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gSpnWBP5ELSI"
      },
      "source": [
        "# 実践演習 Day 1：streamlitとFastAPIのデモ\n",
        "このノートブックでは以下の内容を学習します。\n",
        "\n",
        "- 必要なライブラリのインストールと環境設定\n",
        "- Hugging Faceからモデルを用いたStreamlitのデモアプリ\n",
        "- FastAPIとngrokを使用したAPIの公開方法\n",
        "\n",
        "演習を始める前に、HuggingFaceとngrokのアカウントを作成し、\n",
        "それぞれのAPIトークンを取得する必要があります。\n",
        "\n",
        "\n",
        "演習の時間では、以下の3つのディレクトリを順に説明します。\n",
        "\n",
        "1. 01_streamlit_UI\n",
        "2. 02_streamlit_app\n",
        "3. 03_FastAPI\n",
        "\n",
        "2つ目や3つ目からでも始められる様にノートブックを作成しています。\n",
        "\n",
        "復習の際にもこのノートブックを役立てていただければと思います。\n",
        "\n",
        "### 注意事項\n",
        "「02_streamlit_app」と「03_FastAPI」では、GPUを使用します。\n",
        "\n",
        "これらを実行する際は、Google Colab画面上のメニューから「編集」→ 「ノートブックの設定」\n",
        "\n",
        "「ハードウェアアクセラレーター」の項目の中から、「T4 GPU」を選択してください。\n",
        "\n",
        "このノートブックのデフォルトは「CPU」になっています。\n",
        "\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OhtHkJOgELSL"
      },
      "source": [
        "# 環境変数の設定（1~3共有）\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Y-FjBp4MMQHM"
      },
      "source": [
        "GitHubから演習用のコードをCloneします。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "AIXMavdDEP8U",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "de7379ee-2f82-4338-9c8a-bb4939e3e2f1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: destination path 'lecture-ai-engineering' already exists and is not an empty directory.\n"
          ]
        }
      ],
      "source": [
        "!git clone https://github.com/matsuolab/lecture-ai-engineering.git"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XC8n7yZ_vs1K"
      },
      "source": [
        "必要なAPIトークンを.envに設定します。\n",
        "\n",
        "「lecture-ai-engineering/day1」の配下に、「.env_template」ファイルが存在しています。\n",
        "\n",
        "隠しファイルのため表示されていない場合は、画面左側のある、目のアイコンの「隠しファイルの表示」ボタンを押してください。\n",
        "\n",
        "「.env_template」のファイル名を「.env」に変更します。「.env」ファイルを開くと、以下のような中身になっています。\n",
        "\n",
        "\n",
        "```\n",
        "HUGGINGFACE_TOKEN=\"hf-********\"\n",
        "NGROK_TOKEN=\"********\"\n",
        "```\n",
        "ダブルクオーテーションで囲まれた文字列をHuggingfaceのアクセストークンと、ngrokの認証トークンで書き変えてください。\n",
        "\n",
        "それぞれのアカウントが作成済みであれば、以下のURLからそれぞれのトークンを取得できます。\n",
        "\n",
        "- Huggingfaceのアクセストークン\n",
        "https://huggingface.co/docs/hub/security-tokens\n",
        "\n",
        "- ngrokの認証トークン\n",
        "https://dashboard.ngrok.com/get-started/your-authtoken\n",
        "\n",
        "書き換えたら、「.env」ファイルをローカルのPCにダウンロードしてください。\n",
        "\n",
        "「01_streamlit_UI」から「02_streamlit_app」へ進む際に、CPUからGPUの利用に切り替えるため、セッションが一度切れてしまいます。\n",
        "\n",
        "その際に、トークンを設定した「.env」ファイルは再作成することになるので、その手間を減らすために「.env」ファイルをダウンロードしておくと良いです。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Py1BFS5RqcSS"
      },
      "source": [
        "「.env」ファイルを読み込み、環境変数として設定します。次のセルを実行し、最終的に「True」が表示されていればうまく読み込めています。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "bvEowFfg5lrq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6479d1ee-2224-4d9a-96e3-6cd36a909926"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (1.1.0)\n",
            "/content/lecture-ai-engineering/day1\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ],
      "source": [
        "!pip install python-dotenv\n",
        "from dotenv import load_dotenv, find_dotenv\n",
        "\n",
        "%cd /content/lecture-ai-engineering/day1\n",
        "load_dotenv(find_dotenv())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "os0Yk6gaELSM"
      },
      "source": [
        "# 01_streamlit_UI\n",
        "\n",
        "ディレクトリ「01_streamlit_UI」に移動します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "S28XgOm0ELSM"
      },
      "outputs": [],
      "source": [
        "%cd /content/lecture-ai-engineering/day1/01_streamlit_UI"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eVp-aEIkELSM"
      },
      "source": [
        "必要なライブラリをインストールします。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nBe41LFiELSN"
      },
      "outputs": [],
      "source": [
        "%%capture\n",
        "!pip install -r requirements.txt"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Yyw6VHaTELSN"
      },
      "source": [
        "ngrokのトークンを使用して、認証を行います。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aYw1q0iXELSN"
      },
      "outputs": [],
      "source": [
        "!ngrok authtoken $$NGROK_TOKEN"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RssTcD_IELSN"
      },
      "source": [
        "アプリを起動します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "f-E7ucR6ELSN"
      },
      "outputs": [],
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "public_url = ngrok.connect(8501).public_url\n",
        "print(f\"公開URL: {public_url}\")\n",
        "!streamlit run app.py"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kbYyXVFjELSN"
      },
      "source": [
        "公開URLの後に記載されているURLにブラウザでアクセスすると、streamlitのUIが表示されます。\n",
        "\n",
        "app.pyのコメントアウトされている箇所を編集することで、UIがどの様に変化するか確認してみましょう。\n",
        "\n",
        "streamlitの公式ページには、ギャラリーページがあります。\n",
        "\n",
        "streamlitを使うとpythonという一つの言語であっても、様々なUIを実現できることがわかると思います。\n",
        "\n",
        "https://streamlit.io/gallery"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MmtP5GLOELSN"
      },
      "source": [
        "後片付けとして、使う必要のないngrokのトンネルを削除します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8Ek9QgahELSO"
      },
      "outputs": [],
      "source": [
        "from pyngrok import ngrok\n",
        "ngrok.kill()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "o-T8tFpyELSO"
      },
      "source": [
        "# 02_streamlit_app"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QqogFQKnELSO"
      },
      "source": [
        "\n",
        "ディレクトリ「02_streamlit_app」に移動します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "UeEjlJ7uELSO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bcae4a73-68b5-43ca-d4ad-98a23915f598"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/lecture-ai-engineering/day1/02_streamlit_app\n"
          ]
        }
      ],
      "source": [
        "%cd /content/lecture-ai-engineering/day1/02_streamlit_app"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-XUH2AstELSO"
      },
      "source": [
        "必要なライブラリをインストールします。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "id": "mDqvI4V3ELSO"
      },
      "outputs": [],
      "source": [
        "%%capture\n",
        "!pip install -r requirements.txt"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZO31umGZELSO"
      },
      "source": [
        "ngrokとhuggigfaceのトークンを使用して、認証を行います。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "jPxTiEWQELSO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "09728608-afc3-499a-d9d8-ba28f6aefeb2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n",
            "The token has not been saved to the git credentials helper. Pass `add_to_git_credential=True` in this function directly or `--add-to-git-credential` if using via `huggingface-cli` if you want to set the git credential as well.\n",
            "Token is valid (permission: read).\n",
            "The token `AIE_hirotani` has been saved to /root/.cache/huggingface/stored_tokens\n",
            "Your token has been saved to /root/.cache/huggingface/token\n",
            "Login successful.\n",
            "The current active token is: `AIE_hirotani`\n"
          ]
        }
      ],
      "source": [
        "!ngrok authtoken $$NGROK_TOKEN\n",
        "!huggingface-cli login --token $$HUGGINGFACE_TOKEN"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dz4WrELLELSP"
      },
      "source": [
        "stramlitでHuggingfaceのトークン情報を扱うために、streamlit用の設定ファイル（.streamlit）を作成し、トークンの情報を格納します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "W184-a7qFP0W"
      },
      "outputs": [],
      "source": [
        "# .streamlit/secrets.toml ファイルを作成\n",
        "import os\n",
        "import toml\n",
        "\n",
        "# 設定ファイルのディレクトリ確保\n",
        "os.makedirs('.streamlit', exist_ok=True)\n",
        "\n",
        "# 環境変数から取得したトークンを設定ファイルに書き込む\n",
        "secrets = {\n",
        "    \"huggingface\": {\n",
        "        \"token\": os.environ.get(\"HUGGINGFACE_TOKEN\", \"\")\n",
        "    }\n",
        "}\n",
        "\n",
        "# 設定ファイルを書き込む\n",
        "with open('.streamlit/secrets.toml', 'w') as f:\n",
        "    toml.dump(secrets, f)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fK0vI_xKELSP"
      },
      "source": [
        "アプリを起動します。\n",
        "\n",
        "02_streamlit_appでは、Huggingfaceからモデルをダウンロードするため、初回起動には2分程度時間がかかります。\n",
        "\n",
        "この待ち時間を利用して、app.pyのコードを確認してみましょう。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TBQyTTWTELSP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b62fe58a-ace6-4dac-c931-cc572d2b5f92"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "公開URL: https://f8af-34-82-118-41.ngrok-free.app\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.82.118.41:8501\u001b[0m\n",
            "\u001b[0m\n",
            "NLTK loaded successfully.\n",
            "2025-04-28 05:22:23.548358: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
            "WARNING: All log messages before absl::InitializeLog() is called are written to STDERR\n",
            "E0000 00:00:1745817743.572055    7652 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
            "E0000 00:00:1745817743.579093    7652 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
            "2025-04-28 05:22:23.602707: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\n",
            "To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n",
            "NLTK Punkt data checked/downloaded.\n",
            "Database 'chat_feedback.db' initialized successfully.\n",
            "config.json: 100% 805/805 [00:00<00:00, 4.94MB/s]\n",
            "model.safetensors.index.json: 100% 24.2k/24.2k [00:00<00:00, 85.4MB/s]\n",
            "Fetching 2 files:   0% 0/2 [00:00<?, ?it/s]\n",
            "model-00002-of-00002.safetensors:   0% 0.00/241M [00:00<?, ?B/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   0% 0.00/4.99G [00:00<?, ?B/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:   4% 10.5M/241M [00:00<00:02, 91.0MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   0% 21.0M/4.99G [00:00<00:44, 111MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  13% 31.5M/241M [00:00<00:01, 131MB/s] \u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   1% 41.9M/4.99G [00:00<00:34, 144MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  22% 52.4M/241M [00:00<00:01, 159MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   1% 62.9M/4.99G [00:00<00:36, 134MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  30% 73.4M/241M [00:00<00:01, 138MB/s]\u001b[A\n",
            "model-00002-of-00002.safetensors:  39% 94.4M/241M [00:00<00:01, 131MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   2% 83.9M/4.99G [00:00<00:43, 112MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  48% 115M/241M [00:00<00:00, 134MB/s] \u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   2% 105M/4.99G [00:00<00:40, 120MB/s] \u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  57% 136M/241M [00:01<00:00, 137MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   3% 126M/4.99G [00:01<00:39, 124MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  65% 157M/241M [00:01<00:00, 133MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   3% 147M/4.99G [00:01<00:38, 125MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  74% 178M/241M [00:01<00:00, 133MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   3% 168M/4.99G [00:01<00:38, 125MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  83% 199M/241M [00:01<00:00, 131MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   4% 189M/4.99G [00:01<00:36, 131MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors:  91% 220M/241M [00:01<00:00, 128MB/s]\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   4% 210M/4.99G [00:01<00:36, 131MB/s]\u001b[A\u001b[A\n",
            "model-00002-of-00002.safetensors: 100% 241M/241M [00:01<00:00, 127MB/s]\u001b[A\n",
            "\n",
            "model-00002-of-00002.safetensors: 100% 241M/241M [00:01<00:00, 130MB/s]\n",
            "\n",
            "\n",
            "model-00001-of-00002.safetensors:   5% 252M/4.99G [00:01<00:34, 138MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   6% 283M/4.99G [00:02<00:29, 161MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   6% 315M/4.99G [00:02<00:25, 180MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   7% 346M/4.99G [00:02<00:22, 205MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   8% 377M/4.99G [00:02<00:20, 226MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   8% 409M/4.99G [00:02<00:19, 239MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   9% 440M/4.99G [00:02<00:18, 245MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:   9% 472M/4.99G [00:02<00:18, 246MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  10% 503M/4.99G [00:02<00:18, 245MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  11% 535M/4.99G [00:03<00:17, 260MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  11% 566M/4.99G [00:03<00:21, 207MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  12% 598M/4.99G [00:03<00:20, 219MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  13% 629M/4.99G [00:03<00:18, 231MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  13% 661M/4.99G [00:03<00:18, 232MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  14% 692M/4.99G [00:03<00:17, 248MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  15% 724M/4.99G [00:03<00:16, 264MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  15% 755M/4.99G [00:03<00:15, 269MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  16% 797M/4.99G [00:04<00:14, 285MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  17% 828M/4.99G [00:04<00:14, 293MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  17% 860M/4.99G [00:04<00:15, 266MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  18% 902M/4.99G [00:04<00:14, 282MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  19% 933M/4.99G [00:04<00:14, 286MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  19% 965M/4.99G [00:04<00:13, 290MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  20% 1.01G/4.99G [00:04<00:13, 300MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  21% 1.04G/4.99G [00:04<00:13, 300MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  22% 1.08G/4.99G [00:05<00:12, 309MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  22% 1.12G/4.99G [00:05<00:12, 310MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  23% 1.15G/4.99G [00:05<00:12, 300MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  24% 1.18G/4.99G [00:05<00:12, 300MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  24% 1.22G/4.99G [00:05<00:12, 302MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  25% 1.25G/4.99G [00:05<00:12, 305MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  26% 1.28G/4.99G [00:05<00:12, 295MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  26% 1.31G/4.99G [00:05<00:13, 268MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  27% 1.34G/4.99G [00:05<00:13, 262MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  28% 1.37G/4.99G [00:06<00:14, 249MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  28% 1.41G/4.99G [00:06<00:13, 260MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  29% 1.44G/4.99G [00:06<00:13, 266MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  29% 1.47G/4.99G [00:06<00:14, 249MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  30% 1.50G/4.99G [00:06<00:13, 261MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  31% 1.53G/4.99G [00:06<00:13, 255MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  31% 1.56G/4.99G [00:06<00:14, 241MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  32% 1.59G/4.99G [00:07<00:14, 234MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  33% 1.64G/4.99G [00:07<00:12, 259MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  33% 1.67G/4.99G [00:07<00:13, 251MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  34% 1.70G/4.99G [00:08<00:49, 67.0MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  34% 1.72G/4.99G [00:08<00:43, 75.4MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  35% 1.75G/4.99G [00:08<00:33, 95.9MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  36% 1.78G/4.99G [00:09<00:26, 120MB/s] \u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  37% 1.82G/4.99G [00:09<00:20, 157MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  37% 1.86G/4.99G [00:09<00:17, 180MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  38% 1.89G/4.99G [00:09<00:15, 205MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  38% 1.92G/4.99G [00:09<00:13, 228MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  39% 1.95G/4.99G [00:09<00:12, 242MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  40% 1.99G/4.99G [00:09<00:11, 266MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  41% 2.02G/4.99G [00:09<00:10, 277MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  41% 2.06G/4.99G [00:09<00:10, 281MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  42% 2.09G/4.99G [00:10<00:10, 286MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  42% 2.12G/4.99G [00:10<00:15, 189MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  43% 2.16G/4.99G [00:10<00:12, 220MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  44% 2.19G/4.99G [00:10<00:11, 235MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  45% 2.23G/4.99G [00:10<00:10, 256MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  46% 2.28G/4.99G [00:10<00:09, 277MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  46% 2.31G/4.99G [00:10<00:09, 282MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  47% 2.35G/4.99G [00:11<00:08, 295MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  48% 2.39G/4.99G [00:11<00:08, 308MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  49% 2.43G/4.99G [00:11<00:08, 300MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  49% 2.46G/4.99G [00:11<00:08, 300MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  50% 2.51G/4.99G [00:11<00:08, 304MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  51% 2.54G/4.99G [00:11<00:08, 306MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  52% 2.58G/4.99G [00:11<00:07, 314MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  53% 2.62G/4.99G [00:11<00:08, 281MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  53% 2.65G/4.99G [00:12<00:09, 257MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  54% 2.68G/4.99G [00:12<00:08, 268MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  54% 2.72G/4.99G [00:12<00:08, 274MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  55% 2.75G/4.99G [00:12<00:09, 248MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  56% 2.78G/4.99G [00:12<00:08, 263MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  56% 2.81G/4.99G [00:12<00:08, 250MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  57% 2.84G/4.99G [00:12<00:08, 255MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  58% 2.87G/4.99G [00:12<00:08, 251MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  58% 2.90G/4.99G [00:13<00:07, 265MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  59% 2.94G/4.99G [00:13<00:09, 221MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  59% 2.97G/4.99G [00:13<00:10, 196MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  60% 3.00G/4.99G [00:13<00:11, 173MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  61% 3.02G/4.99G [00:13<00:11, 174MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  61% 3.04G/4.99G [00:14<00:12, 159MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  61% 3.06G/4.99G [00:14<00:11, 163MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  62% 3.08G/4.99G [00:14<00:11, 163MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  62% 3.10G/4.99G [00:14<00:13, 140MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  63% 3.12G/4.99G [00:14<00:12, 147MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  63% 3.15G/4.99G [00:14<00:11, 155MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  63% 3.17G/4.99G [00:14<00:11, 160MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  64% 3.19G/4.99G [00:14<00:11, 163MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  64% 3.21G/4.99G [00:15<00:10, 163MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  65% 3.23G/4.99G [00:15<00:10, 169MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  66% 3.27G/4.99G [00:15<00:07, 217MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  66% 3.30G/4.99G [00:15<00:08, 202MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  67% 3.34G/4.99G [00:15<00:07, 227MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  68% 3.38G/4.99G [00:15<00:07, 214MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  68% 3.41G/4.99G [00:15<00:07, 214MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  69% 3.44G/4.99G [00:16<00:06, 227MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  70% 3.47G/4.99G [00:16<00:06, 234MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  70% 3.50G/4.99G [00:16<00:06, 240MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  71% 3.53G/4.99G [00:16<00:05, 242MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  71% 3.57G/4.99G [00:16<00:05, 249MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  72% 3.60G/4.99G [00:16<00:05, 261MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  73% 3.64G/4.99G [00:16<00:04, 282MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  74% 3.67G/4.99G [00:16<00:04, 279MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  74% 3.70G/4.99G [00:17<00:04, 284MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  75% 3.74G/4.99G [00:17<00:04, 301MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  76% 3.79G/4.99G [00:17<00:03, 305MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  77% 3.83G/4.99G [00:17<00:03, 309MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  78% 3.87G/4.99G [00:17<00:03, 313MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  78% 3.90G/4.99G [00:17<00:03, 312MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  79% 3.94G/4.99G [00:17<00:03, 318MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  80% 3.98G/4.99G [00:17<00:03, 288MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  81% 4.02G/4.99G [00:18<00:03, 271MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  81% 4.05G/4.99G [00:18<00:03, 276MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  82% 4.08G/4.99G [00:18<00:03, 246MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  83% 4.12G/4.99G [00:18<00:03, 265MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  83% 4.15G/4.99G [00:18<00:03, 268MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  84% 4.18G/4.99G [00:18<00:03, 246MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  85% 4.22G/4.99G [00:18<00:03, 253MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  85% 4.25G/4.99G [00:19<00:02, 254MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  86% 4.28G/4.99G [00:19<00:02, 252MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  86% 4.31G/4.99G [00:19<00:02, 256MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  87% 4.34G/4.99G [00:19<00:02, 253MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  88% 4.37G/4.99G [00:19<00:02, 237MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  88% 4.40G/4.99G [00:19<00:02, 245MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  89% 4.45G/4.99G [00:19<00:02, 235MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  90% 4.48G/4.99G [00:20<00:02, 217MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  91% 4.52G/4.99G [00:20<00:01, 245MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  91% 4.55G/4.99G [00:20<00:01, 226MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  92% 4.58G/4.99G [00:20<00:02, 168MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  93% 4.62G/4.99G [00:20<00:01, 203MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  93% 4.66G/4.99G [00:20<00:01, 186MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  94% 4.68G/4.99G [00:21<00:02, 121MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  95% 4.72G/4.99G [00:21<00:01, 158MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  95% 4.76G/4.99G [00:21<00:01, 187MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  96% 4.79G/4.99G [00:21<00:00, 202MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  97% 4.82G/4.99G [00:21<00:00, 223MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  97% 4.85G/4.99G [00:21<00:00, 239MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  98% 4.89G/4.99G [00:22<00:00, 254MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  99% 4.92G/4.99G [00:22<00:00, 264MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors:  99% 4.95G/4.99G [00:22<00:00, 272MB/s]\u001b[A\u001b[A\n",
            "\n",
            "model-00001-of-00002.safetensors: 100% 4.99G/4.99G [00:22<00:00, 222MB/s]\n",
            "Fetching 2 files: 100% 2/2 [00:22<00:00, 11.32s/it]\n",
            "Loading checkpoint shards: 100% 2/2 [00:00<00:00, 12.33it/s]\n",
            "generation_config.json: 100% 168/168 [00:00<00:00, 1.28MB/s]\n",
            "tokenizer_config.json: 100% 46.9k/46.9k [00:00<00:00, 23.7MB/s]\n",
            "tokenizer.model: 100% 4.24M/4.24M [00:00<00:00, 68.6MB/s]\n",
            "tokenizer.json: 100% 17.5M/17.5M [00:00<00:00, 120MB/s]\n",
            "special_tokens_map.json: 100% 555/555 [00:00<00:00, 4.16MB/s]\n",
            "Device set to use cuda\n",
            "2025-04-28 05:23:14.401 Examining the path of torch.classes raised:\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/streamlit/web/bootstrap.py\", line 347, in run\n",
            "    if asyncio.get_running_loop().is_running():\n",
            "       ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "RuntimeError: no running event loop\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/streamlit/watcher/local_sources_watcher.py\", line 217, in get_module_paths\n",
            "    potential_paths = extract_paths(module)\n",
            "                      ^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/streamlit/watcher/local_sources_watcher.py\", line 210, in <lambda>\n",
            "    lambda m: list(m.__path__._path),\n",
            "                   ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/torch/_classes.py\", line 13, in __getattr__\n",
            "    proxy = torch._C._get_custom_class_python_wrapper(self.name, attr)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "RuntimeError: Tried to instantiate class '__path__._path', but it does not exist! Ensure that it is registered via torch::class_\n",
            "NLTK loaded successfully.\n",
            "NLTK Punkt data checked/downloaded.\n",
            "Database 'chat_feedback.db' initialized successfully.\n",
            "2025-04-28 05:23:48.096 Examining the path of torch.classes raised:\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/streamlit/web/bootstrap.py\", line 347, in run\n",
            "    if asyncio.get_running_loop().is_running():\n",
            "       ^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "RuntimeError: no running event loop\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/streamlit/watcher/local_sources_watcher.py\", line 217, in get_module_paths\n",
            "    potential_paths = extract_paths(module)\n",
            "                      ^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/streamlit/watcher/local_sources_watcher.py\", line 210, in <lambda>\n",
            "    lambda m: list(m.__path__._path),\n",
            "                   ^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/torch/_classes.py\", line 13, in __getattr__\n",
            "    proxy = torch._C._get_custom_class_python_wrapper(self.name, attr)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "RuntimeError: Tried to instantiate class '__path__._path', but it does not exist! Ensure that it is registered via torch::class_\n"
          ]
        }
      ],
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "public_url = ngrok.connect(8501).public_url\n",
        "print(f\"公開URL: {public_url}\")\n",
        "!streamlit run app.py"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6UrGt06hz2pT"
      },
      "source": [
        "アプリケーションの機能としては、チャット機能や履歴閲覧があります。\n",
        "\n",
        "これらの機能を実現するためには、StreamlitによるUI部分だけではなく、SQLiteを使用したチャット履歴の保存やLLMのモデルを呼び出した推論などの処理を組み合わせることで実現しています。\n",
        "\n",
        "- **`app.py`**: アプリケーションのエントリーポイント。チャット機能、履歴閲覧、サンプルデータ管理のUIを提供します。\n",
        "- **`ui.py`**: チャットページや履歴閲覧ページなど、アプリケーションのUIロジックを管理します。\n",
        "- **`llm.py`**: LLMモデルのロードとテキスト生成を行うモジュール。\n",
        "- **`database.py`**: SQLiteデータベースを使用してチャット履歴やフィードバックを保存・管理します。\n",
        "- **`metrics.py`**: BLEUスコアやコサイン類似度など、回答の評価指標を計算するモジュール。\n",
        "- **`data.py`**: サンプルデータの作成やデータベースの初期化を行うモジュール。\n",
        "- **`config.py`**: アプリケーションの設定（モデル名やデータベースファイル名）を管理します。\n",
        "- **`requirements.txt`**: このアプリケーションを実行するために必要なPythonパッケージ。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Xvm8sWFPELSP"
      },
      "source": [
        "後片付けとして、使う必要のないngrokのトンネルを削除します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WFJC2TmZELSP"
      },
      "outputs": [],
      "source": [
        "from pyngrok import ngrok\n",
        "ngrok.kill()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rUXhIzV7ELSP"
      },
      "source": [
        "# 03_FastAPI\n",
        "\n",
        "ディレクトリ「03_FastAPI」に移動します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4ejjDLxr3kfC"
      },
      "outputs": [],
      "source": [
        "%cd /content/lecture-ai-engineering/day1/03_FastAPI"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f45TDsNzELSQ"
      },
      "source": [
        "必要なライブラリをインストールします。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9uv6glCz5a7Z"
      },
      "outputs": [],
      "source": [
        "%%capture\n",
        "!pip install -r requirements.txt"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "JfrmE2VmELSQ"
      },
      "source": [
        "ngrokとhuggigfaceのトークンを使用して、認証を行います。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ELzWhMFORRIO"
      },
      "outputs": [],
      "source": [
        "!ngrok authtoken $$NGROK_TOKEN\n",
        "!huggingface-cli login --token $$HUGGINGFACE_TOKEN"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t-wztc2CELSQ"
      },
      "source": [
        "アプリを起動します。\n",
        "\n",
        "「02_streamlit_app」から続けて「03_FastAPI」を実行している場合は、モデルのダウンロードが済んでいるため、すぐにサービスが立ち上がります。\n",
        "\n",
        "「03_FastAPI」のみを実行している場合は、初回の起動時にモデルのダウンロードが始まるので、モデルのダウンロードが終わるまで数分間待ちましょう。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "meQ4SwISn3IQ"
      },
      "outputs": [],
      "source": [
        "!python app.py"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RLubjIhbELSR"
      },
      "source": [
        "FastAPIが起動すると、APIとクライアントが通信するためのURL（エンドポイント）が作られます。\n",
        "\n",
        "URLが作られるのと合わせて、Swagger UIというWebインターフェースが作られます。\n",
        "\n",
        "Swagger UIにアクセスすることで、APIの仕様を確認できたり、APIをテストすることができます。\n",
        "\n",
        "Swagger UIを利用することで、APIを通してLLMを動かしてみましょう。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XgumW3mGELSR"
      },
      "source": [
        "後片付けとして、使う必要のないngrokのトンネルを削除します。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "RJymTZio-WPJ"
      },
      "outputs": [],
      "source": [
        "from pyngrok import ngrok\n",
        "ngrok.kill()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4"
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "nbformat": 4,
  "nbformat_minor": 0
}